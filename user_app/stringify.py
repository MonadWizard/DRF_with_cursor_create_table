from .apps import appp_nameee

def create_table_stringfy(req_data):
    for table_name in req_data:
        columns_dict = req_data[table_name]

    column_nt = ""
    for entry in columns_dict["fields"]:

        column = entry.get("name")
        type = entry.get("type")
        operator = entry.get("operator")
        column_nt += f'"{column}" {type} {operator},\n'

    create_table = f"""CREATE SEQUENCE {table_name}_id_seq;
                    CREATE TABLE IF NOT EXISTS public.{table_name} (
                    id bigint NOT NULL DEFAULT nextval('{table_name}_id_seq'::regclass),
                    {column_nt[:-2]}, 
                    create_at timestamp with time zone NOT NULL,
                    update_at timestamp with time zone NOT NULL,
                    CONSTRAINT {table_name}_pkey PRIMARY KEY (id)
                    )
                    TABLESPACE pg_default;

                    ALTER TABLE IF EXISTS public.{table_name}
                        OWNER to postgres;
                    """

    return create_table



def create_relational_query(req_data):
    for table_name in req_data:
        columns_dict = req_data[table_name]
    # print('---------',columns_dict["fields"])
    
    column_names = ""
    column_values = ""
    for entry in columns_dict["fields"]:
        for k,v in entry.items():
            column_names += f"{k}, "
            column_values += f"'{v}', "
    
    create_relational = f"""INSERT INTO public.{table_name}(
        {column_names} create_at, update_at) 
        VALUES ({column_values} now(), now());"""
    # print("---------",create_relational, "---------")

    return create_relational















