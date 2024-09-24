CREATE TABLE IF NOT EXISTS devices (
    id UUID NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ,
    title VARCHAR NOT NULL,
    module_id UUID NOT NULL,
    user_id UUID NOT NULL,
    device_type VARCHAR NOT NULL,
    device_vendor VARCHAR NOT NULL,
    serial_number VARCHAR NOT NULL,
    device_link VARCHAR NOT NULL,
    PRIMARY KEY (id)
);
