from johnsnowlabs.abstract_base.base_enum import BaseEnum


class EMRClusterStates(BaseEnum):
    # https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-overview.html#emr-overview-cluster-lifecycle
    STARTING = "STARTING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    WAITING = "WAITING"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
