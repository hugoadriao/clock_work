from config.api_config import api

clock_namespace = api.namespace(
    'clock',
    description=(
        'Information from clock table'
    )
)

person_namespace = api.namespace(
    'person',
    description=(
        'Information about persons'
    )
)
