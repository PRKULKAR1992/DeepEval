from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric, ExactMatchMetric
from deepeval.test_case import LLMTestCase
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

firstTest = LLMTestCase(
    input="what is capital of india?",
    expected_output="Delhi",
    actual_output="Delhi"

)
    
evaluate([firstTest], metrics= [AnswerRelevancyMetric()])
