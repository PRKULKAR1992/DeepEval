from deepeval import evaluate
from deepeval.metrics import ExactMatchMetric
from deepeval.test_case import LLMTestCase


firstTest = LLMTestCase(
    input="what is capital of india?",
    expected_output="Delhi",
    actual_output="Delhi"

)
    
evaluate([firstTest], metrics= [ExactMatchMetric()])
