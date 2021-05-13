from datetime import date

# User settings
BASELINE_FILENAME_TEMPLATE = "pubmed21n{0:04d}.xml.gz"
BASELINE_URL = "ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/" # Must include last /
BMCS_RESULTS_FILENAME = "bmcs_results_12th_April_21.txt.gz"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EUTILS_DELAY = 0.34 # seconds
EUTILS_RETMAX = 10000
JOURNAL_MEDLINE_FILENAME = "J_Medline_16th_April_21.txt.gz"
NUM_BASLINE_FILES = 1062
PROBLEMATIC_JOURNALS_FILENAME = "problematic_journals.csv"
SELECTIVE_INDEXING_PERIODS_FILENAME = "2021_selective_indexing_periods_input.csv"
TEST_SET_YEAR = 2020
USE_EUTILS = True
VOTING_TRAIN_YEARS = [2019]
MODEL_MAX_YEAR = TEST_SET_YEAR - 1

# System settings
CNN_DATA_DIR = "cnn_model"
DATE_FORMAT = "%Y-%m-%d"
DOWNLOADED_DATA_FILENAME_TEMPLATE = "{0:04d}.xml.gz"
ENCODING = "utf8"
EXTRACTED_DATA_FILENAME_TEMPLATE = "{0:04d}.json.gz"
EXCLUDED_REF_TYPES = ["CommentOn",
"ErratumFor",
"ExpressionOfConcernFor",
"RepublishedFrom",
"RetractionOf",
"UpdateOf",
"OriginalReportIn"
"ReprintOf"]
JOURNAL_ID_DICT_FILENAME = "journal_id_dict.pkl"
JOURNAL_ID_TXT_FILENAME = "journal_ids.txt"
MEDLINE_DATA_DIR = "medline_data"
OPT_THRESHOLDS_DELTA = .00005
OPT_THRESHOLDS_FILENAME_TEMPLATE = "{}_optimum_thresholds.txt"
OPT_THRESHOLDS_TARGET_PRECISION = 0.97
OPT_THRESHOLDS_TARGET_RECALL = 0.995
TEST_SET_FILENAME = "test_set.json.gz"
TEST_SET_SIZE = 40000
TRAIN_SET_FILENAME = "train_set.json.gz"
VAL_SET_FILENAME = "val_set.json.gz"
VOTING_DATA_DIR = "voting_model"
VOTING_MODEL_FILENAME = "voting_model.joblib"
WORD_INDEX_DICT_FILENAME = "word_index_dict.pkl"
WORD_INDEX_TXT_FILENAME = "word_indices.txt"
WORD_INDEX_TXT_VOCAB_SIZE = 400000

PP_CONFIG = { "min_pub_year": 1809, 
              "max_pub_year": MODEL_MAX_YEAR, 
              "min_year_indexed": 1965, 
              "max_year_indexed": MODEL_MAX_YEAR, 
              "date_format": DATE_FORMAT }