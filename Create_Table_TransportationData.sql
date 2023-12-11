Create Table TransportationData
(
 id int not null identity(1,1),
 reportyear int NULL,
 race_eth_code nvarchar(50) NULL,
 race_eth_name nvarchar(50) NULL, 
 geoname nvarchar(50) NULL, 
 mode nvarchar(50) NULL, 
 mode_name nvarchar(50) NULL, 
 pop_total int NULL, 
 pop_mode int NULL,
 EventProcessedUtcTime datetime2 NULL,
 PartitionId Int NULL,
 EventEnqueuedUtcTime datetime2 NULL
)