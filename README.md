# End-to-End Analytics Pipeline

This repository contains Docker configurations for setting up an analytics pipeline using Apache Pulsar and ClickHouse, designed to ingest, process, and analyze real-time data streams.

## Table of Contents

- [Getting Started](#getting-started)
  - [Python Environment Setup](#python-environment-setup)
- [How to get started](#how-to)
- [Understanding the Analytics Pipeline](#understanding-the-analytics-pipeline)
- [Connecting Apache Pulsar with ClickHouse](#connecting-apache-pulsar-with-clickhouse)
- [Considerations for Handling Millions of Data Per Day](#considerations-for-handling-millions-of-data-per-day)


## Getting Started

To start using this setup, follow these steps:

1. **Clone this repository:**
   ```bash
   git clone git@github.com:Deniskerec/pulsar-clickhouse.git
   ```

2. **Navigate to the cloned directory:**
   ```bash
   cd newAFC_end_2_end
   ```

3. **Start/Stop the Docker containers:**
   ```bash
   docker-compose up -d
   ```
   ```bash
   docker-compose down
   ```
 

This will initialize Apache Pulsar and ClickHouse services in Docker containers.

### Python Environment Setup

Set up a Python environment to interact with Apache Pulsar and ClickHouse by executing the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pulsar-client clickhouse-driver
```

### How to 
Every sub directory has its own README.mb where the process is described in detail.

We can test Pulsar sending msg. directly to Clickhouse 
__
Other cases are migration of data from remote datases to local pgsql database and migrating data to Clickhouse for performance testing.

## Understanding the Analytics Pipeline

The analytics pipeline leverages Apache Pulsar for distributed messaging and ClickHouse for high-performance columnar storage, enabling real-time data analytics. Pulsar serves as the data ingestion layer, capable of handling millions of messages per second, while ClickHouse provides fast query processing for analytics.

## Connecting Apache Pulsar with ClickHouse

To connect Apache Pulsar with ClickHouse, we leverage Pulsar's ability to act as a unified messaging platform, streaming data into ClickHouse for storage and analysis. This setup involves configuring Pulsar to produce messages into a topic, which are then consumed and stored in ClickHouse, either directly via custom consumers or through Pulsar's Kafka compatibility layer and ClickHouse's Kafka engine.

## Considerations for Handling Millions of Data Per Day

When handling millions of data per day, both direct consumption via custom consumers and using Pulsar's Kafka compatibility have their merits. The best choice depends on specific requirements such as latency, throughput, ease of setup, and maintenance. Direct consumption allows for highly customizable and potentially lower latency solutions, while leveraging Pulsar's Kafka compatibility offers simplified architecture and reduced development time at the cost of additional overhead and possible compatibility limitations.

Both direct consumption via custom consumers and using Pulsar's Kafka compatibility have their merits, and the best choice depends on your specific requirements, such as latency, throughput, ease of setup, and maintenance:

Direct Consumption via Custom Consumers:

Pros:
Highly customizable: You have full control over the consumption process, including error handling, retries, and data transformation before storage.
Potentially lower latency: Direct consumption can be optimized for lower latency if the consumer application is efficiently designed.
Cons:
Development overhead: Requires more effort to develop and maintain consumer applications.
Complexity: Managing a custom consumer application adds complexity, especially at scale.
Pulsar's Kafka Compatibility Layer:

Pros:
Simplified architecture: Leverages existing Kafka integrations, making it easier to integrate with systems already using Kafka, like ClickHouse.
Reduced development time: Less need to develop custom consumer logic, as ClickHouse can directly consume from Pulsar topics using its Kafka engine.
Cons:
Overhead: The compatibility layer might introduce additional overhead compared to direct consumption.
Compatibility limitations: While Pulsar aims to provide comprehensive Kafka compatibility, there may be edge cases or specific Kafka features not fully supported.
For handling millions of data per day, both approaches are capable, but the choice depends on your specific scenario. If you already use Kafka or want a simpler setup with less custom development, leveraging Pulsar's Kafka compatibility might be preferable. However, if you need custom processing logic, lower latency, or want to avoid any compatibility layer overhead, direct consumption with custom consumers could be more beneficial.

