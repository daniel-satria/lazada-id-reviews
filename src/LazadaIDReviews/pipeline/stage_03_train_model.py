import os
from LazadaIDReviews.config.configuration import ConfigurationManager
from LazadaIDReviews.components.training import Training
from LazadaIDReviews import logger

STAGE_NAME = "Training"

class TrainingPipeline:
    def __init__(self):
        pass

    def pipeline(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.logistic_regression()
        except Exception as e:
            logger.error(e)
            raise e
        
        
if __name__ == '__main__':
    try:
        os.chdir("/home/ubuntu/learning/mlops/pacmann/lazada-id-reviews")
        logger.info(f"\n\n")
        logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        
        obj = TrainingPipeline()
        obj.pipeline()
        
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
