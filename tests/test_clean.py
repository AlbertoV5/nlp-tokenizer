"""
DISCLAIMER: Data is de-identified.
"""
import pandas as pd
import logging

import kardiasclean


log = logging.getLogger(__name__)


def test_main():
    data = pd.DataFrame(
        {
            "patient_id": (0, 1, 2, 3, 4),
            "surgery": (
                "Reparación de CIA, parche",
                "Reparación de Tetralogía de Fallot, ventriculotomia parche transanular",
                " Reparación de CIV, parche + Reparación de estenosis aórtica subvalvular",
                "Reparación de CIV con parche + Cierre quirúrgico de Conducto Arterioso",
                "Reparación de CIV, parche + Ampliación del tracto de salida del VD + Reparación de CIA, primaria",
            ),
        }
    ).set_index("patient_id")
    assert data.index.name == "patient_id"
    data["surgery"] = kardiasclean.split_string(data["surgery"])
    log.debug(data)
    data_map = kardiasclean.spread_column(data["surgery"])
    log.debug(data_map)
    # Clean
    data_map["surgery"] = kardiasclean.clean_accents(data_map["surgery"])
    data_map["surgery"] = kardiasclean.clean_symbols(data_map["surgery"])
    data_map["keywords"] = kardiasclean.clean_stopwords(
        data_map["surgery"], extra=["parche"]
    )
    data_map["token"] = kardiasclean.clean_tokenize(data_map["keywords"])
    data_list = kardiasclean.create_unique_list(data_map, data_map["token"]).drop(
        ["patient_id"], axis=1
    )
    log.debug(data_list["keywords"])
    # normalize map
    data_map["surgery"] = kardiasclean.normalize_from_tokens(
        data_map["token"], data_list["token"], data_list["surgery"]
    )
    log.debug(data_map["surgery"])
    # Pre-process
    bins = kardiasclean.perform_binning_quantile(data_map["surgery"], quantile=0.9)
    log.debug(f"\n{bins}")
    high_freq, low_freq = kardiasclean.perform_frequency_split_quantile(
        data_map["surgery"], quantile=0.9
    )
    evaluation = kardiasclean.evaluate_distribution(high_freq, low_freq)
    log.debug(evaluation)
    log.debug(data_map.columns)
    matrix = kardiasclean.perform_matrix_encoding(
        data_map["surgery"], data_map["patient_id"]
    )
    log.debug(matrix)
