#!/usr/bin/env bash

aws batch  register-job-definition --cli-input-json file://./job_document_sentiment_analysis.json