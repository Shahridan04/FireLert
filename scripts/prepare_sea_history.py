"""Resumable, isolated Indonesia/Malaysia history preparation; never deploys."""
import datetime as dt
import json
import shutil
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from pipeline.streaming.download_guarded import download
from pipeline.streaming.aggregate_archives import prepare, write_json
from pipeline.streaming.prepare_analysis import build as reduce_counts
from pipeline.streaming.evaluate_counts import evaluate, seal_locked_artifacts
from pipeline.streaming.__main__ import require_complete_history
from pipeline.streaming.prepared_runtime import run_preaggregated
from pipeline.streaming.prepared_globe import build_annual
from pipeline.streaming.summarize_regions import summarize
from pipeline.streaming.stage_calendars import build as calendars
from pipeline.streaming.estimate_dictionary import estimate

COUNTRIES = ['Indonesia', 'Malaysia']
WORK = ROOT / 'work' / 'sea-history-v1'


def status(stage, **extra):
    write_json(WORK/'STATUS.json', dict(stage=stage, updated_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
               countries=COUNTRIES, publication='Isolated outputs only; application data unchanged.', **extra))
    print(stage, flush=True)


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    if shutil.disk_usage(WORK).free < 10*1024**3:
        raise RuntimeError('Less than 10 GiB free. No acquisition started.')
    status('downloading')
    download(COUNTRIES, range(2001,2026), WORK/'archives', workers=3, reserve_gib=10)
    manifest=json.loads((WORK/'archives/manifest.json').read_text(encoding='utf-8'))
    require_complete_history(manifest, COUNTRIES)
    write_json(WORK/'reports/data_manifest.json', manifest)
    status('preparing_exact_counts')
    prepare(WORK/'archives/manifest.json', COUNTRIES, WORK/'prepared', chunk_size=100000, write_clean=False)
    status('reducing_analysis_tables')
    # Each expensive completed stage is checkpointed. Failed stages retain diagnostics.
    if not (WORK/'analysis/SEA_COMPLETE.json').exists():
        reduce_counts([str(WORK/'prepared')], WORK/'analysis')
        write_json(WORK/'analysis/SEA_COMPLETE.json', {'complete':True})
    analyses = [str(WORK/'analysis')]
    reports = WORK/'reports'
    status('fitting_and_evaluating')
    if not (reports/'LOCKED_ARTIFACTS.json').exists():
        evaluate(analyses, reports)
    model_path = reports/'harmonization_model.json'
    model = json.loads(model_path.read_text(encoding='utf-8'))
    model.update(model_revision='firelert-sea-v1', calibration_countries=COUNTRIES,
                 scope_note='Indonesia/Malaysia only; not the retained five-country model.',
                 rhythm_note='Weekly-rest-day inference not run; no hypothesis or rest-day assignment assumed.')
    write_json(model_path, model)
    seal_locked_artifacts(reports)
    status('generating_daily_history')
    run_preaggregated(analyses, model_path, WORK/'processed')
    status('generating_globe_and_calendar')
    summarize([str(WORK/'prepared')], reports/'regions.json')
    build_annual(analyses, model_path, WORK/'public_original/data/globe.json')
    write_json(reports/'rhythm_results.json', {'gate':{'decision':'insufficient_data'}, 'countries':{},
               'reason':'Not evaluated for this regional scope.'})
    calendars(WORK/'processed', reports/'harmonization_eval.csv', reports/'rhythm_results.json',
              reports/'regions.json', WORK/'public_original/data')
    estimate(WORK/'public_original/data', WORK/'public/data')
    status('ready_for_review', evaluation=str(reports/'harmonization_eval.csv'),
           outputs=str(WORK/'public/data'))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        status('failed', error=str(error))
        traceback.print_exc()
        sys.exit(1)
