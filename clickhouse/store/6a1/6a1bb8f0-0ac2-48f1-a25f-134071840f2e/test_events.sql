ATTACH TABLE _ UUID '9dcaf0ef-5690-4b54-83c6-bd5b519ac751'
(
    `EventDate` Date,
    `EventTime` DateTime,
    `EventType` String,
    `EventData` String
)
ENGINE = MergeTree
PARTITION BY toYYYYMMDD(EventDate)
ORDER BY (EventTime, EventType)
SETTINGS index_granularity = 8192
