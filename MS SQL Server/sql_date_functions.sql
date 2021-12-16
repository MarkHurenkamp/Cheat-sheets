------------------------------------------------------------------------------
-- Snippets for SQL Server 
------------------------------------------------------------------------------

select 
  getdate() as [Server time]
, getutcdate() as [UTC datetime]

------------------------------------------------------------------------------
-- Time zone conversion
------------------------------------------------------------------------------
-- SQL Server 2016+, convert time from first time zone to second time zone
-- SELECT * FROM sys.time_zone_info for all time zones. 
, getutcdate() 
    at time zone 'UTC' 
    at time zone 'Central European Standard Time' as [Current CEST time]

-- Convert from PST to CEST. Summer time is automatically accounted for.

-- Both at 'winter time' UTC -7 and UTC +2
, cast('2021-01-01 10:00:00:00' as datetime) 
    at time zone 'Pacific Standard Time' 
    at time zone 'Central European Standard Time' as [Both Winter]
-- Returns '2021-01-01T19:00:00+01:00'

-- West coast to PDT (UTC -6), CEST still in winter time (UTC +2)
, cast('2021-03-15 10:00:00:00' as datetime) 
    at time zone 'Pacific Standard Time' 
    at time zone 'Central European Standard Time' as [PST Summer - CEST Winter]
-- Returns '2021-03-15T18:00:00+01:00'

-- Both at 'summer time' (UTC -6 and UTC +1)
, cast('2021-07-01 10:00:00:00' as datetime) 
    at time zone 'Pacific Standard Time' 
    at time zone 'Central European Standard Time' as [Both Summer]
-- Returns '2021-07-01T19:00:00+02:00'
;


------------------------------------------------------------------------------
-- Start/end dates
-- eomonth = SQL Server 2012+
------------------------------------------------------------------------------
declare @somedate date = '2021-10-28'

select 
    @somedate as [somedate]

-- historic dates
,   dateadd(yy, datediff(yy, 0, @somedate), 0) as [start of year]
,   eomonth(@somedate, -1) as [end of previous month]
,   dateadd(qq, datediff(qq, 0, @somedate) -1, 0) as [start of previous quarter]
,   dateadd(dd, -1, dateadd(qq, datediff(qq, 0, @somedate), 0)) as [end of previous quarter]
,   dateadd(qq, datediff(qq, 0, @somedate), 0) as [start of current quarter]


-- future dates
,   eomonth(@somedate) as [end of current month]
,   eomonth(@somedate, 1) as [end of next month]
,   dateadd(dd, -1, dateadd(qq, datediff(qq, 0, @somedate) +1, 0)) as [end of current quarter]
,   dateadd(qq, datediff(qq, 0, @somedate) +1, 0) as [start of next quarter]
,   dateadd(dd, -1, dateadd(qq, datediff(qq, 0, @somedate) +2, 0)) as [end of next quarter]
,   dateadd(yy, datediff(yy, 0, @somedate) +1, -1) as [end of year]