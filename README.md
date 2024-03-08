# NewAFC End-to-End Analytics Pipeline

This repository contains Docker configurations for setting up an analytics pipeline using Apache Pulsar and ClickHouse, designed to ingest, process, and analyze real-time data streams.

## Table of Contents

- [Getting Started](#getting-started)
  - [Python Environment Setup](#python-environment-setup)
  - [Initial Data Ingestion Test](#initial-data-ingestion-test)
- [Understanding the Analytics Pipeline](#understanding-the-analytics-pipeline)
- [Connecting Apache Pulsar with ClickHouse](#connecting-apache-pulsar-with-clickhouse)
- [Stopping Services](#stopping-services)

## Getting Started

To start using this setup, follow these steps:

1. Clone this repository: 

   git clone git@github.com:Deniskerec/pulsar-clickhouse.git

Navigate to the cloned directory:


cd newAFC_end_2_end
Start the Docker containers:


docker-compose up -d

This will initialize Apache Pulsar and ClickHouse services in Docker containers.

Python Environment Setup
Set up a Python environment to interact with Apache Pulsar and ClickHouse by executing the following commands:


python3 -m venv venv
source venv/bin/activate
pip install pulsar-client clickhouse-driver
Initial Data Ingestion Test
After starting your Docker containers, perform a basic test to verify that the setup correctly processes data.

Access ClickHouse CLI:
Connect to the ClickHouse client:


docker exec -it newafc_end_2_end-clickhouse-server-1 clickhouse-client
Create a Test Database and Table (skip if already created):


CREATE DATABASE IF NOT EXISTS test;

USE test;

CREATE TABLE test_events (
    EventDate Date,
    EventTime DateTime,
    EventType String,
    EventData String
) ENGINE = MergeTree()
PARTITION BY toYYYYMMDD(EventDate)
ORDER BY (EventTime, EventType);
Exit the ClickHouse client.

Produce Test Messages to Pulsar:


docker exec -it newafc_end_2_end-pulsar-1 bin/pulsar-client produce my-topic --messages "hello from pulsar"
Adjust the topic and message content as needed for your specific test.

Verify Data Ingestion in ClickHouse:
After setting up the data flow from Pulsar, check that data has arrived in ClickHouse:


docker exec -it newafc_end_2_end-clickhouse-server-1 clickhouse-client
-- Then in the ClickHouse CLI


SELECT * FROM test.test_events;
Understanding the Analytics Pipeline
The analytics pipeline leverages Apache Pulsar for distributed messaging and ClickHouse for high-performance columnar storage, enabling real-time data analytics. Pulsar serves as the data ingestion layer, capable of handling millions of messages per second, while ClickHouse provides fast query processing for analytics.

Connecting Apache Pulsar with ClickHouse
To connect Apache Pulsar with ClickHouse, we leverage Pulsar's ability to act as a unified messaging platform, streaming data into ClickHouse for storage and analysis. This setup involves configuring Pulsar to produce messages into a topic, which are then consumed and stored in ClickHouse, either directly via custom consumers or through Pulsar's Kafka compatibility layer and ClickHouse's Kafka engine.

Stopping Services
To stop the Docker containers and halt the services, run:


docker-compose down
vbnet


This README.md provides a comprehensive guide for setting up and testing your end-to-end analytics pipeline, including the necessary steps to get started, perform initial data ingestion tests, and understand how Apache Pulsar and ClickHouse work together in this architecture.