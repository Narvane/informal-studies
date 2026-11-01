# AWS Fundamentals and Application Development

A roadmap from cloud concepts and core AWS services through application development, deployment, observability, and architecture decisions.

<!-- The source marked AWS-4.3 with [S]; interpreted as studied but not yet assessed. -->

## Topics

## 1. Cloud Computing and AWS Fundamentals

- [ ] [ ] **AWS-1.1** — Cloud computing models: IaaS, PaaS and SaaS
- [ ] [ ] **AWS-1.2** — Public, private and hybrid cloud
- [ ] [ ] **AWS-1.3** — AWS global infrastructure: Regions, Availability Zones and edge locations
- [ ] [ ] **AWS-1.4** — Shared responsibility model
- [ ] [ ] **AWS-1.5** — AWS service categories and architectural principles
- [ ] [ ] **AWS-1.6** — High availability, fault tolerance, scalability and elasticity
- [ ] [ ] **AWS-1.7** — Well-Architected Framework pillars
- [ ] [ ] **AWS-1.8** — AWS account structure, organizations and multi-account concepts
- [ ] [ ] **AWS-1.9** — AWS pricing models, billing and cost optimization concepts

## 2. Identity, Security and Governance

- [ ] [ ] **AWS-2.1** — IAM users, groups, roles and policies
- [ ] [ ] **AWS-2.2** — Identity-based and resource-based policies
- [ ] [ ] **AWS-2.3** — Policy evaluation, explicit deny and least privilege
- [ ] [ ] **AWS-2.4** — Temporary credentials, STS and role assumption
- [ ] [ ] **AWS-2.5** — IAM roles for AWS workloads
- [ ] [ ] **AWS-2.6** — AWS SDK credential provider chains
- [ ] [ ] **AWS-2.7** — AWS Secrets Manager and Systems Manager Parameter Store
- [ ] [ ] **AWS-2.8** — AWS KMS, encryption at rest and encryption in transit
- [ ] [ ] **AWS-2.9** — AWS Certificate Manager and TLS concepts
- [ ] [ ] **AWS-2.10** — AWS CloudTrail and auditing
- [ ] [ ] **AWS-2.11** — Amazon Cognito: user pools and identity pools
- [ ] [ ] **AWS-2.12** — AWS WAF, Shield and application security fundamentals

## 3. Networking Fundamentals

- [ ] [ ] **AWS-3.1** — Amazon VPC, CIDR and IP addressing
- [ ] [ ] **AWS-3.2** — Public and private subnets
- [ ] [ ] **AWS-3.3** — Route tables, internet gateways and NAT gateways
- [ ] [ ] **AWS-3.4** — Security groups versus network ACLs
- [ ] [ ] **AWS-3.5** — DNS and Amazon Route 53
- [ ] [ ] **AWS-3.6** — VPC endpoints and AWS PrivateLink
- [ ] [ ] **AWS-3.7** — VPC peering and Transit Gateway concepts
- [ ] [ ] **AWS-3.8** — Load balancing: ALB, NLB and their use cases
- [ ] [ ] **AWS-3.9** — CloudFront, edge locations and content delivery
- [ ] [ ] **AWS-3.10** — Connectivity between application components and managed services

## 4. Compute and Application Hosting

- [ ] [ ] **AWS-4.1** — Amazon EC2: instances, AMIs and instance types
- [ ] [ ] **AWS-4.2** — Auto Scaling and Elastic Load Balancing
- [x] [ ] **AWS-4.3** — AWS Lambda architecture and execution model
- [ ] [ ] **AWS-4.4** — Lambda handlers, triggers, execution roles and configuration
- [ ] [ ] **AWS-4.5** — Lambda concurrency, throttling, timeout and memory
- [ ] [ ] **AWS-4.6** — Lambda retries, failure destinations and dead-letter queues
- [ ] [ ] **AWS-4.7** — Lambda versions, aliases and deployment concepts
- [ ] [ ] **AWS-4.8** — Amazon ECS, EKS and container fundamentals
- [ ] [ ] **AWS-4.9** — AWS Fargate and serverless containers
- [ ] [ ] **AWS-4.10** — AWS Elastic Beanstalk
- [ ] [ ] **AWS-4.11** — Choosing between EC2, Lambda and containers

## 5. Storage and Content Delivery

- [ ] [ ] **AWS-5.1** — Amazon S3: buckets, objects and storage classes
- [ ] [ ] **AWS-5.2** — S3 permissions, bucket policies and Block Public Access
- [ ] [ ] **AWS-5.3** — S3 versioning, lifecycle rules and replication
- [ ] [ ] **AWS-5.4** — S3 presigned URLs and temporary access
- [ ] [ ] **AWS-5.5** — S3 event notifications
- [ ] [ ] **AWS-5.6** — Amazon EBS, EFS and instance store
- [ ] [ ] **AWS-5.7** — Amazon FSx and managed file storage concepts
- [ ] [ ] **AWS-5.8** — Amazon CloudFront: caching, origins and invalidations
- [ ] [ ] **AWS-5.9** — Choosing storage services for different requirements

## 6. Databases and Caching

- [ ] [ ] **AWS-6.1** — Relational and non-relational database concepts
- [ ] [ ] **AWS-6.2** — Amazon RDS and database engines
- [ ] [ ] **AWS-6.3** — Amazon Aurora and its architectural characteristics
- [ ] [ ] **AWS-6.4** — RDS backups, Multi-AZ, read replicas and failover
- [ ] [ ] **AWS-6.5** — Amazon DynamoDB: tables, items, attributes and keys
- [ ] [ ] **AWS-6.6** — DynamoDB partition keys and sort keys
- [ ] [ ] **AWS-6.7** — DynamoDB secondary indexes: GSI and LSI
- [ ] [ ] **AWS-6.8** — DynamoDB Query versus Scan
- [ ] [ ] **AWS-6.9** — DynamoDB capacity modes, consistency and transactions
- [ ] [ ] **AWS-6.10** — DynamoDB Streams and change data capture
- [ ] [ ] **AWS-6.11** — Amazon ElastiCache and caching strategies
- [ ] [ ] **AWS-6.12** — Database connection management and connection pooling
- [ ] [ ] **AWS-6.13** — Choosing between RDS, Aurora, DynamoDB and caching services

## 7. Messaging and Event-Driven Architecture

- [ ] [ ] **AWS-7.1** — Synchronous versus asynchronous communication
- [ ] [ ] **AWS-7.2** — Amazon SQS: standard and FIFO queues
- [ ] [ ] **AWS-7.3** — SQS visibility timeout, long polling and message retention
- [ ] [ ] **AWS-7.4** — SQS dead-letter queues and redrive policies
- [ ] [ ] **AWS-7.5** — Amazon SNS: topics, subscriptions and fan-out
- [ ] [ ] **AWS-7.6** — Amazon EventBridge: event buses, rules and targets
- [ ] [ ] **AWS-7.7** — AWS Step Functions and workflow orchestration
- [ ] [ ] **AWS-7.8** — Amazon Kinesis and streaming fundamentals
- [ ] [ ] **AWS-7.9** — Event-driven architecture and loose coupling
- [ ] [ ] **AWS-7.10** — At-most-once, at-least-once and exactly-once processing concepts
- [ ] [ ] **AWS-7.11** — Idempotency, duplicate messages and message ordering
- [ ] [ ] **AWS-7.12** — Retries, exponential backoff, jitter and failure handling
- [ ] [ ] **AWS-7.13** — Choosing between SQS, SNS, EventBridge and Step Functions

## 8. APIs and Application Integration

- [ ] [ ] **AWS-8.1** — Amazon API Gateway architecture
- [ ] [ ] **AWS-8.2** — API Gateway routes, stages, integrations and deployments
- [ ] [ ] **AWS-8.3** — REST APIs versus HTTP APIs and WebSocket APIs
- [ ] [ ] **AWS-8.4** — API authentication and authorization concepts
- [ ] [ ] **AWS-8.5** — API throttling, quotas, caching and request validation
- [ ] [ ] **AWS-8.6** — AWS AppSync and GraphQL fundamentals
- [ ] [ ] **AWS-8.7** — Direct service integrations and service-to-service communication
- [ ] [ ] **AWS-8.8** — API versioning, compatibility and error-handling concepts

## 9. AWS SDKs and Application Development

- [ ] [ ] **AWS-9.1** — AWS SDKs, service clients and API operations
- [ ] [ ] **AWS-9.2** — AWS SDK for Java 2.x: core concepts
- [ ] [ ] **AWS-9.3** — Credentials, regions and SDK configuration
- [ ] [ ] **AWS-9.4** — Synchronous versus asynchronous SDK clients
- [ ] [ ] **AWS-9.5** — Pagination, retries, timeouts and exception handling
- [ ] [ ] **AWS-9.6** — Client lifecycle, resource management and connection reuse
- [ ] [ ] **AWS-9.7** — AWS service integration patterns for backend applications
- [ ] [ ] **AWS-9.8** — Environment configuration and configuration precedence
- [ ] [ ] **AWS-9.9** — Local development and AWS service emulation concepts
- [ ] [ ] **AWS-9.10** — Unit, integration and contract testing concepts
- [ ] [ ] **AWS-9.11** — Dependency injection and AWS SDK integration in Spring applications

## 10. Deployment and Infrastructure as Code

- [ ] [ ] **AWS-10.1** — Infrastructure as Code principles
- [ ] [ ] **AWS-10.2** — AWS CloudFormation: templates, stacks and change sets
- [ ] [ ] **AWS-10.3** — AWS SAM and serverless application concepts
- [ ] [ ] **AWS-10.4** — AWS CDK and programmatic infrastructure definitions
- [ ] [ ] **AWS-10.5** — CI/CD fundamentals
- [ ] [ ] **AWS-10.6** — AWS CodeBuild, CodePipeline and CodeDeploy
- [ ] [ ] **AWS-10.7** — Lambda deployment packages and container images
- [ ] [ ] **AWS-10.8** — Rolling, canary and blue/green deployments
- [ ] [ ] **AWS-10.9** — Versions, aliases, rollback and release management
- [ ] [ ] **AWS-10.10** — Configuration and environment separation
- [ ] [ ] **AWS-10.11** — Deployment strategies for minimizing downtime and risk

## 11. Monitoring, Logging and Troubleshooting

- [ ] [ ] **AWS-11.1** — Amazon CloudWatch: metrics, logs, dashboards and alarms
- [ ] [ ] **AWS-11.2** — CloudWatch Logs Insights
- [ ] [ ] **AWS-11.3** — AWS X-Ray and distributed tracing
- [ ] [ ] **AWS-11.4** — AWS CloudTrail versus CloudWatch
- [ ] [ ] **AWS-11.5** — Application observability and structured logging
- [ ] [ ] **AWS-11.6** — Lambda monitoring, errors, timeouts and throttling
- [ ] [ ] **AWS-11.7** — Diagnosing IAM permission failures
- [ ] [ ] **AWS-11.8** — Diagnosing networking and connectivity failures
- [ ] [ ] **AWS-11.9** — Diagnosing messaging and event-processing failures
- [ ] [ ] **AWS-11.10** — Performance bottlenecks and latency analysis
- [ ] [ ] **AWS-11.11** — Reliability, resource utilization and cost monitoring

## 12. Architecture and Service Selection

- [ ] [ ] **AWS-12.1** — AWS Well-Architected design trade-offs
- [ ] [ ] **AWS-12.2** — Monoliths, distributed systems and serverless architectures
- [ ] [ ] **AWS-12.3** — Stateless versus stateful application components
- [ ] [ ] **AWS-12.4** — Scalability, availability and fault isolation
- [ ] [ ] **AWS-12.5** — Resilience, retries and graceful degradation
- [ ] [ ] **AWS-12.6** — Caching, asynchronous processing and decoupling
- [ ] [ ] **AWS-12.7** — Data consistency and transaction trade-offs
- [ ] [ ] **AWS-12.8** — Security versus convenience trade-offs
- [ ] [ ] **AWS-12.9** — Performance versus cost trade-offs
- [ ] [ ] **AWS-12.10** — Choosing AWS services from architectural requirements
