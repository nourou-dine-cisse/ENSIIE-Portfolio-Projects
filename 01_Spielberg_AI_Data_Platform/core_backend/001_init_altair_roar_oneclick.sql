-- Spielberg MCP Postgres Schema
-- Tables for Altair, ROAR, and OneClick data sources

-- ============================================================================
-- ALTAIR PROJECTS
-- ============================================================================

CREATE TABLE IF NOT EXISTS altair_projects (
    id SERIAL PRIMARY KEY,
    project_id VARCHAR(50) UNIQUE NOT NULL,
    bf_id VARCHAR(50) UNIQUE NOT NULL,
    client VARCHAR(255) NOT NULL,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    currency VARCHAR(3) DEFAULT 'EUR',
    sold_amount DECIMAL(12, 2),
    cost_budget DECIMAL(12, 2),
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_altair_projects_bf_id ON altair_projects(bf_id);
CREATE INDEX idx_altair_projects_client ON altair_projects(client);
CREATE INDEX idx_altair_projects_status ON altair_projects(status);

-- Work codes (nested in JSON, now normalized)
CREATE TABLE IF NOT EXISTS altair_project_work_codes (
    id SERIAL PRIMARY KEY,
    project_id VARCHAR(50) NOT NULL REFERENCES altair_projects(project_id) ON DELETE CASCADE,
    code VARCHAR(50) NOT NULL,
    label VARCHAR(255),
    unit VARCHAR(50),
    rate DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vendors (nested in JSON, now normalized)
CREATE TABLE IF NOT EXISTS altair_project_vendors (
    id SERIAL PRIMARY KEY,
    project_id VARCHAR(50) NOT NULL REFERENCES altair_projects(project_id) ON DELETE CASCADE,
    vendor_type VARCHAR(50),
    role VARCHAR(255),
    days DECIMAL(8, 2),
    rate DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- ROAR TIMESHEETS
-- ============================================================================

CREATE TABLE IF NOT EXISTS roar_timesheets (
    id SERIAL PRIMARY KEY,
    employee_key VARCHAR(50) NOT NULL,
    date DATE NOT NULL,
    bf_id VARCHAR(50),
    project_id VARCHAR(50),
    work_code VARCHAR(50),
    hours DECIMAL(8, 2),
    status VARCHAR(50) DEFAULT 'submitted',
    source VARCHAR(100),
    confidence_note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_roar_timesheets_employee ON roar_timesheets(employee_key);
CREATE INDEX idx_roar_timesheets_date ON roar_timesheets(date);
CREATE INDEX idx_roar_timesheets_bf_id ON roar_timesheets(bf_id);
CREATE INDEX idx_roar_timesheets_project_id ON roar_timesheets(project_id);

-- ============================================================================
-- ONECLICK PEOPLE
-- ============================================================================

CREATE TABLE IF NOT EXISTS oneclick_people (
    id SERIAL PRIMARY KEY,
    employee_key VARCHAR(50) UNIQUE NOT NULL,
    display_name VARCHAR(255),
    contract_type VARCHAR(50),
    start_date DATE,
    end_date DATE,
    location VARCHAR(255),
    pivot_id VARCHAR(50),
    role VARCHAR(255),
    department VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_oneclick_people_employee_key ON oneclick_people(employee_key);
CREATE INDEX idx_oneclick_people_department ON oneclick_people(department);
CREATE INDEX idx_oneclick_people_role ON oneclick_people(role);

-- ============================================================================
-- ONECLICK ABSENCES
-- ============================================================================

CREATE TABLE IF NOT EXISTS oneclick_absences (
    id SERIAL PRIMARY KEY,
    employee_key VARCHAR(50) NOT NULL REFERENCES oneclick_people(employee_key) ON DELETE CASCADE,
    date DATE NOT NULL,
    type VARCHAR(50),
    status VARCHAR(50) DEFAULT 'approved',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_oneclick_absences_employee ON oneclick_absences(employee_key);
CREATE INDEX idx_oneclick_absences_date ON oneclick_absences(date);
CREATE INDEX idx_oneclick_absences_type ON oneclick_absences(type);

-- ============================================================================
-- BDC REQUESTS (keep existing SQLite logic but add reference)
-- ============================================================================

CREATE TABLE IF NOT EXISTS bdc_requests (
    id SERIAL PRIMARY KEY,
    spielberg_request_id VARCHAR(100) UNIQUE NOT NULL,
    bf_id VARCHAR(50),
    campaign_name VARCHAR(255),
    document_type VARCHAR(100),
    supplier_name VARCHAR(255),
    amount_ht DECIMAL(12, 2),
    requester_email VARCHAR(255),
    requester_name VARCHAR(255),
    request_status VARCHAR(50) DEFAULT 'NEW',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    kissflow_id VARCHAR(100),
    UNIQUE(kissflow_id)
);

CREATE INDEX idx_bdc_requests_bf_id ON bdc_requests(bf_id);
CREATE INDEX idx_bdc_requests_status ON bdc_requests(request_status);
