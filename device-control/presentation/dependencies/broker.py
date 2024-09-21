from application.device.usecases.interfaces import DevicePublishInterface
from infrastructure.kafka.publisher import KafkaPublisher


def get_broker() -> DevicePublishInterface:
    return KafkaPublisher()
