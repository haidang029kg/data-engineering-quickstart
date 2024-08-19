import glob

import numpy as np
import pandas as pd
import xarray as xr

NC_DIR_PATH = "/home/vnhd/nc_files"
FILES = glob.glob(f"{NC_DIR_PATH}/*.nc4")


def main():
    res = extract(FILES[0])
    res = transform(res)
    load(res)


def extract(nc_file_path: str) -> xr.Dataset:
    print("==========extract data")
    return xr.open_dataset(nc_file_path)


def transform(ds: xr.Dataset) -> pd.DataFrame:
    print("==========transform data")
    d_humidity: xr.DataArray = ds.QV
    d_air_temp: xr.DataArray = ds.T

    # humidity transform
    df_humidity = d_humidity.to_dataframe(name="value")
    df_humidity = df_humidity.rename(columns={"value": "humidity"})
    df_humidity["humidity_unit"] = "kg kg-1"
    df_humidity = df_humidity.reset_index()

    print(df_humidity)

    # air temperature transform
    df_air_temp = d_air_temp.to_dataframe(name="value")
    df_air_temp = df_air_temp.rename(columns={"value": "air_temp"})
    df_air_temp["air_temp_unit"] = "K"
    df_air_temp = df_air_temp.reset_index()

    print(df_air_temp)

    try:
        # merge
        merged_df = pd.merge(
            df_humidity,
            df_air_temp,
            on=["time", "lev", "lat", "lon"],
        )
        return merged_df

    except Exception as exc:
        print(exc)
        raise exc


def load(data: pd.DataFrame):
    print("==========load data")
    print(data.head())


if __name__ == "__main__":
    main()
