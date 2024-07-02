# sales_oltp


--create schema sales
--GO

CREATE TABLE [sales].[customer](
	[cust_id] [int] IDENTITY(1,1) NOT NULL,
	[first_name] [varchar](200) NOT NULL,
	[last_name] [varchar](200) NOT NULL,
	[email_id] [varchar](200) NOT NULL,
	[created_on_date] [date] NULL,
	[created_on_time] [time](7) NULL,
	[last_updated_on_date] [date] NULL,
	[last_updated_on_time] [time](7) NULL,
	
) ON [PRIMARY]
GO

ALTER TABLE [sales].[customer] ADD  DEFAULT (getdate()) FOR [created_on_date]
GO

ALTER TABLE [sales].[customer] ADD  DEFAULT (getdate()) FOR [created_on_time]
GO

ALTER TABLE [sales].[customer] ADD CONSTRAINT PK_Customer PRIMARY KEY ([cust_id])
GO
----------------------------------------------------------

USE [POC]
GO

CREATE TABLE [sales].[orders](
	[order_id] [int] IDENTITY(1,1) NOT NULL,
	[fk_cust_id] [int] NOT NULL,
	[date] [date] NULL,
	[time] [time](7) NULL,
	[created_on_date] [date] NULL,
	[created_on_time] [time](7) NULL,
	[last_updated_on_date] [date] NULL,
	[last_updated_on_time] [time](7) NULL,
PRIMARY KEY CLUSTERED 
(
	[order_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [sales].[orders]  WITH CHECK ADD FOREIGN KEY([fk_cust_id])
REFERENCES [sales].[customer] ([cust_id])
GO

---------------------------------------------------------------

USE [POC]
GO

CREATE TABLE [sales].[product_types](
	[product_type_id] [int] IDENTITY(1,1) NOT NULL,
	[product_name] [nvarchar](255) NULL,
	[category] [nvarchar](255) NULL,
	[product_component] [nvarchar](500) NULL,
	[created_on_date] [date] NULL,
	[created_on_time] [time](7) NULL,
	[last_updated_on_date] [date] NULL,
	[last_updated_on_time] [time](7) NULL,
PRIMARY KEY CLUSTERED 
(
	[product_type_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
-------------------------------------------------------

USE [POC]
GO

CREATE TABLE [sales].[product](
	[product_id] [int] IDENTITY(1,1) NOT NULL,
	[fk_product_type_id] [int] NOT NULL,
	[model] [varchar](20) NULL,
	[price] [int] NULL,
	[created_on_date] [date] NULL,
	[created_on_time] [time](7) NULL,
	[last_updated_on_date] [date] NULL,
	[last_updated_on_time] [time](7) NULL,
PRIMARY KEY CLUSTERED 
(
	[product_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [sales].[product]  WITH CHECK ADD FOREIGN KEY([fk_product_type_id])
REFERENCES [sales].[product_types] ([product_type_id])
GO

--------------------------------------------------------
USE [POC]
GO

CREATE TABLE [sales].[order_specs](
	[order_specs_id] [int] IDENTITY(1,1) NOT NULL,
	[fk_order_id] [int] NOT NULL,
	[fk_product_id] [int] NOT NULL,
	[quantity] [int] NULL,
	[created_on_date] [date] NULL,
	[created_on_time] [time](7) NULL,
	[last_updated_on_date] [date] NULL,
	[last_updated_on_time] [time](7) NULL,
) ON [PRIMARY]
GO

ALTER TABLE [sales].[order_specs] WITH CHECK ADD FOREIGN KEY([fk_order_id])
REFERENCES [sales].[orders]([order_id]) 
GO

ALTER TABLE [sales].[order_specs]  WITH CHECK ADD FOREIGN KEY([fk_product_id])
REFERENCES [sales].[product]([product_id]) 
GO
