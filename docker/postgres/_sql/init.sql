-- public.clients definition

-- Drop table

-- DROP TABLE public.clients;

CREATE TABLE public.clients (
	id serial4 NOT NULL,
	"name" varchar(105) NULL,
	dni varchar(9) NULL,
	code varchar(256) NULL,
	address varchar(105) NULL,
	email varchar(105) NULL,
	CONSTRAINT clients_pkey PRIMARY KEY (id)
);

-- public.products definition

-- Drop table

-- DROP TABLE public.products;

CREATE TABLE public.products (
	id serial4 NOT NULL,
	"name" varchar(250) NULL,
	caliber varchar(250) NULL,
	brand varchar(250) NULL,
	description varchar(250) NULL,
	"type" varchar(250) NULL,
	serial_number varchar(250) NULL,
	CONSTRAINT products_pkey PRIMARY KEY (id)
);


-- public.supplier definition

-- Drop table

-- DROP TABLE public.supplier;

CREATE TABLE public.supplier (
	id serial4 NOT NULL,
	"name" varchar(250) NULL,
	cuil varchar(250) NULL,
	email varchar(250) NULL,
	code varchar(250) NULL,
	CONSTRAINT supplier_code_key UNIQUE (code),
	CONSTRAINT supplier_cuil_key UNIQUE (cuil),
	CONSTRAINT supplier_email_key UNIQUE (email),
	CONSTRAINT supplier_pkey PRIMARY KEY (id)
);