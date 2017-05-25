from analysis.virus_pkg import virus_analysis


def virus_check():
    if virus_analysis.analysis_signature():
        return "THIS IS VIRUS"

    if virus_analysis.analysis_heuristic():
        return "THIS IS VIRUS"

    return "THIS IS NOT VIRUS"
