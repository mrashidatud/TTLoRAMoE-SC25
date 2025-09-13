dataload_type = "single"
multiple_datasets = ['sst2']  # unused in 'single' mode
experts_list = ['sst2','qqp','mrpc','cola','winogrande_l','rte']
import runpy, os, sys
sys.path.insert(0, os.path.dirname(__file__))
runpy.run_path(os.path.join(os.path.dirname(__file__), 'moe_train.py'), run_name="__main__")
