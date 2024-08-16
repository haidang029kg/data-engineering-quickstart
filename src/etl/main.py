import numpy as np
import pandas as pd
import xarray as xr

DIR_NAME = "nc_files"
FILE_NAMES = [
    # "MERRA2_100.inst3_3d_asm_Np.19800101.nc4",
    #
    "MERRA2_400.inst3_3d_asm_Np.20240101.nc4",
    "MERRA2_400.inst3_3d_asm_Np.20240102.nc4",
    # "MERRA2_400.inst3_3d_asm_Np.20240103.nc4",
    # "MERRA2_400.inst3_3d_asm_Np.20240104.nc4",
]


def main():
    print("Hello world")
    files = [f"./{DIR_NAME}/{f_name}" for f_name in FILE_NAMES]

    res = extract(files[0])
    res = transform(res)


def extract(nc_file_path: str) -> xr.Dataset:
    return xr.open_dataset(nc_file_path)


def transform(ds: xr.Dataset) -> pd.DataFrame:
    print(ds)
    d_humidity: xr.DataArray = ds.QV
    d_air_temp: xr.DataArray = ds.T

    print(d_air_temp)


def load(data: pd.DataFrame):
    pass


if __name__ == "__main__":
    main()
