import pandera as pa
from pandera.typing import Int, Float, String, Series


class ECG(pa.DataFrameModel):
    ECG_Inverted_T_Waves: Series[Int] = pa.Field(nullable=True)
    ECG_Pathological_Q_Waves: Series[Int] = pa.Field(nullable=True)
    ECG_PR: Series[Float] = pa.Field(nullable=True)
    ECG_QRS: Series[Float] = pa.Field(nullable=True)
    ECG_QTc: Series[Float] = pa.Field(nullable=True)
    ECG_Rate: Series[Float] = pa.Field(nullable=True)
    ECG_Rhythm: Series[String] = pa.Field(nullable=True)
    ECG_P: Series[Float] = pa.Field(nullable=True)
    ECG_QT: Series[Float] = pa.Field(nullable=True)

    class Config:
        coerce = True