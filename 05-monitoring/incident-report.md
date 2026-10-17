# Incident Report: INC-2026-1017 (Controlled Simulation)

> **Simulation notice:** this incident was deliberately triggered by the ISMS implementer to test the detection chain. No real attacker was involved. This report replaces the earlier INC-2026-1015 draft, which listed alarm names but had no tested detection path.

## 1. Overview

| Field | Value |
|---|---|
| Incident ID | INC-2026-1017 |
| Type | Repeated failed AWS console logins (simulated brute-force attempt) |
| Date | 2026-10-17 |
| Severity | Low (no successful authentication, targeted account has no permissions) |
| Environment | NovaTech Solutions AWS account, eu-north-1 |
| Targeted identity | IAM user `before-test-user` (deliberately weak: console password, no MFA) |
| Reported by | ISMS implementer |

## 2. Detection

### 2.1 Evidence in CloudTrail

5 failed `ConsoleLogin` events for `before-test-user` (source IP redacted in this report):

| Time (UTC) | CloudTrail eventID | Result | Error message |
|---|---|---|---|
| 2026-10-17T16:19:55Z | 039aa422-8e95-4cea-9393-28d498ef370f | Failure | Failed authentication |
| 2026-10-17T16:19:58Z | 70b1880a-ea82-4056-96c6-c27c9e612855 | Failure | Failed authentication |
| 2026-10-17T16:20:01Z | 5be2f2ae-67f3-4f36-8cf7-4779409e17e2 | Failure | Failed authentication |
| 2026-10-17T16:20:03Z | 380bb301-606b-4eb1-97c2-db2b4a501d81 | Failure | Failed authentication |
| 2026-10-17T16:20:05Z | 0d4d3c28-6176-4d4b-b00e-4be68b9a7050 | Failure | Failed authentication |

### 2.2 Detection chain

- CloudTrail trail `novatech-trail` delivers events to the CloudWatch Logs group `/aws/cloudtrail/novatech-trail`.
- Metric filter `FailedConsoleLoginFilter`, pattern `{ ($.eventName = ConsoleLogin) && ($.responseElements.ConsoleLogin = Failure) }`, publishes metric `NovaTech/Security` / `FailedConsoleLoginCount`.
- Alarm `NovaTech-FailedConsoleLogin-Alarm` fires when the sum is 3 or more within 5 minutes.
- The alarm action publishes to SNS topic `novatech-security-alerts` (e-mail subscription confirmed).

### 2.3 Alarm history (UTC)

| Time | Event |
|---|---|
| 16:14:19 | Alarm created |
| 16:15:26 | INSUFFICIENT_DATA to OK |
| 16:23:26 | OK to ALARM |
| 16:23:26 | SNS action executed successfully |

The alarm e-mail confirms the trigger: one 5-minute datapoint with value 5.0 against a threshold of 3.0 (screenshot `05-08`).

Time to detect: **03:31 (mm:ss)** after the first failed attempt and **03:21** after the last one. This includes the CloudTrail-to-CloudWatch delivery delay and the 5-minute alarm period.

## 3. Impact

- 5 failed attempts, 0 successful. IAM shows *Last console sign-in: Never* for `before-test-user`.
- The account has no directly attached permission policies and no access keys.
- No data was accessed and no resources were changed.

## 4. Investigation

1. Filtered CloudTrail Event history by event name `ConsoleLogin` and identified the `before-test-user` events above, all recorded as `Failure`.
2. Matched their timestamps with the alarm history in CloudWatch.
3. Checked the IAM user: no successful sign-in, no permissions, no access keys.
4. Checked other `ConsoleLogin` events in the same period: only the investigator's own `Suleyman-admin` session.

## 5. Response and containment

No containment was needed because the event was a simulation. The response procedure validated by this exercise:

1. Confirm the alert (e-mail and CloudTrail evidence).
2. Look for any successful login by the same user or from the same source IP.
3. If a successful login exists: remove the console login profile, revoke sessions, rotate credentials.
4. Review GuardDuty findings for the same period.
5. Record the incident and lessons learned.

The weak test account will be deleted in the cleanup phase, which also removes the "console access without MFA" audit finding.

## 6. Lessons learned

1. **Gap found:** before this exercise no SNS topic existed and none of the alarms had a notification action, so an alarm could change state without anyone being told. Fixed: topic `novatech-security-alerts`, confirmed e-mail subscription, all alarms linked to it.
2. **Correction:** the earlier draft stated that alerts were sent to a SOC channel. That was not true at the time and has been removed.
3. **Orphan alarm removed:** `NovaTech-RootUser-Activity-Alarm` watched a metric that no filter produced and could never fire.
4. **Detection latency** of a few minutes is acceptable at this scale. An EventBridge rule on sign-in events would make it near real time.
5. **Limitations:** the 3-in-5-minutes threshold does not catch slow attacks; there is a single recipient and no automated response.

## 7. ISO/IEC 27001:2022 mapping

| Control | How this exercise supports it |
|---|---|
| A.5.24 | Incident management procedure defined and tested |
| A.5.25 | Event assessed and classified (Low) |
| A.5.26 | Response steps documented and exercised |
| A.5.27 | Lessons learned recorded (Section 6) |
| A.5.28 | Evidence preserved (CloudTrail eventIDs, CSV, screenshots) |
| A.8.5 | Weak authentication on the test account identified |
| A.8.15 | CloudTrail logging used as the evidence source |
| A.8.16 | Alarm detected anomalous sign-in activity |

## 8. Evidence

- `05-monitoring/simulation-events.csv`
- Screenshots `05-04` to `05-09` in `screenshots/`