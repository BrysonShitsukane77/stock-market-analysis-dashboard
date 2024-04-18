with 

source as (

    select * from {{ source('staging', 'stock_price_data') }}

),

renamed as (

    select
        datetime,
        open,
        high,
        low,
        close,
        volume,
        stock_symbol,
        stock_name

    from source

)

select * from renamed
