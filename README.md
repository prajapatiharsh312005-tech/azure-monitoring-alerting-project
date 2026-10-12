## Project Screenshots

1. Azure App Service

Shows the deployed web application running on Azure.

<img width="1920" height="1080" alt="web app" src="https://github.com/user-attachments/assets/9a6a7d42-07ff-4e48-b15b-079438976106" />

2. Application Health Check

Shows the /health endpoint returning a healthy status.

<img width="1920" height="1080" alt="health endpoints" src="https://github.com/user-attachments/assets/bb106b2e-bdfe-4aa8-925a-356685423f3d" />

3. Azure Monitor Metrics

Shows request counts and HTTP error metrics.

<img width="1920" height="1080" alt="http server errors ss" src="https://github.com/user-attachments/assets/4e369980-bfb2-46f0-8576-7df3392a5ddc" />

4.  HTTP 5xx Alert Rule

Shows the configured Azure Monitor alert rule.

<img width="1920" height="1080" alt="http-5xx-alert-rule" src="https://github.com/user-attachments/assets/767d4980-6fec-4c6d-b927-e1b84d33c955" />


# Azure App Service Monitoring & Alerting

## Project Overview
This project demonstrates how to deploy and monitor a Python Flask web application using Microsoft Azure App Service. Azure Monitor metrics and alert rules were configured to observe application traffic and detect HTTP server errors.

## Objectives
- Deploy a Python Flask application to Azure App Service.
- Verify application health using a `/health` endpoint.
- Monitor incoming requests and HTTP errors using Azure Monitor.
- Configure an alert rule for HTTP 5xx server errors.

## Architecture
**User → Azure App Service (Python Flask) → Azure Monitor Metrics → Metric Alert Rule**

## Azure Services Used
- Azure App Service
- Azure Monitor Metrics
- Azure Monitor Alerts
- Azure Resource Group

## Monitoring Configuration
The following metrics were checked during testing:

| Metric | Aggregation | Observed value |
|---|---|---:|
| Requests | Count | 72 |
| HTTP 4xx errors | Sum | 11 |
| HTTP 5xx server errors | Sum | 0 |

*These values reflect one observation period and may change over time.*

## Alert Configuration
- **Alert rule:** `harsh-web-app-5xx-alert`
- **Signal:** HTTP server errors (5xx)
- **Condition:** Total greater than 1
- **Lookback period:** 5 minutes
- **Evaluation frequency:** Every 1 minute
- **Severity:** Sev 3 – Informational
- **Status:** Enabled

The alert rule is intended to detect elevated server-error counts. Alert notification delivery and an actual alert firing were not verified as part of this project.

## Health Verification
The application's `/health` endpoint returned a healthy status during testing.

Expected response:

```json
{
  "application": "azure-web-application",
  "status": "healthy"
}
```

## Key Learnings
- Deploying and validating a Python web application on Azure App Service.
- Using Azure Monitor to inspect request and HTTP error metrics.
- Configuring a metric-based alert rule.
- Distinguishing HTTP 4xx client errors from HTTP 5xx server errors.

## Future Improvements
- Verify alert notifications using a safe test configuration.
- Add Application Insights telemetry and investigate failed requests.
- Document alert response and troubleshooting procedures.

## Disclaimer
This is a learning project. Metric values are observations from a selected time period and are not permanent performance statistics.
