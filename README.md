# Threat Model and Secure Configuration

## Project Objective
To identify security threats in a small web application
and recommend suitable security controls.

## Application
A simple web application with user login functionality.

## Assets
- User credentials
- Personal information
- Application database
- Session tokens

## Security Goals
- Protect user information
- Prevent unauthorized access
- Maintain data integrity
- Ensure application availability
## 5. Threat Identification Using STRIDE

STRIDE is a threat modelling method used to identify
security threats in a web application.

### 1. Spoofing
An attacker may use stolen user credentials to
impersonate a legitimate user.

Mitigation: Use strong passwords and multi-factor
authentication.

### 2. Tampering
An attacker may modify application data without
permission.

Mitigation: Validate inputs and enforce access controls.

### 3. Repudiation
A user may deny performing an action if proper logs
are not maintained.

Mitigation: Maintain secure audit logs.

### 4. Information Disclosure
Sensitive user information may be exposed to
unauthorized users.

Mitigation: Encrypt sensitive data and restrict access.

### 5. Denial of Service
An attacker may send excessive requests and make
the application unavailable.

Mitigation: Apply rate limiting and request validation.

### 6. Elevation of Privilege
A normal user may attempt to access administrator
functions without authorization.

Mitigation: Enforce role-based access control.## 6. Risk Assessment

Risks are ranked based on their likelihood and impact.

| ID | Threat | Likelihood | Impact | Risk Level |
|----|--------|------------|--------|------------|
| R1 | Spoofing | High | High | High |
| R2 | Tampering | Medium | High | High |
| R3 | Repudiation | Medium | Medium | Medium |
| R4 | Information Disclosure | High | High | High |
| R5 | Denial of Service | Medium | High | High |
| R6 | Elevation of Privilege | Low | High | Medium |

### Risk Assessment Explanation

1. Spoofing: Stolen credentials may allow unauthorized access.
2. Tampering: Unauthorized changes may affect data integrity.
3. Repudiation: Missing logs may make actions difficult to trace.
4. Information Disclosure: Sensitive information may be exposed.
5. Denial of Service: Excessive requests may interrupt availability.
6. Elevation of Privilege: Improper access controls may expose admin functions.

### Risk Treatment

- High Risk: Implement security controls immediately.
- Medium Risk: Apply suitable controls and monitor regularly.
- Low Risk: Monitor and review periodically.