models = {
    "NluRef": {
        0: "en.summarize.clinical_guidelines_large.pipeline",
        1: "en.resolve.cpt.augmented",
        2: "en.resolve.loinc.augmented",
        6: "en.med_ner.nihss_pipeline",
        7: "en.resolve.icd9.pipeline",
        8: "en.resolve.HPO",
        9: "en.explain_doc.clinical_radiology.pipeline",
        12: "en.explain_doc.era",
        13: "en.med_ner.pathogen.pipeline",
        14: "en.resolve.icdo_augmented",
        17: "en.med_ner.sdoh_langtest.pipeline",
        21: "pt.deid.clinical",
        23: "en.de_identify.clinical_pipeline",
        24: "ro.deid.clinical",
        25: "fr.deid_obfuscated",
        26: "es.deid.clinical",
        27: "en.map_entity.snomed_to_icdo",
        28: "en.med_ner.risk_factors.pipeline",
        29: "de.deid.clinical",
        30: "it.deid.clinical",
        31: "en.explain_doc.clinical_ade",
        32: "en.summarize.radiology.pipeline",
        33: "en.med_ner.living_species.pipeline",
        34: "en.med_ner.anatom.pipeline",
        38: "en.med_ner.bionlp.pipeline",
    },
    "ReleaseID": {
        0: "0.9",
        1: "0.9",
        2: "0.9",
        6: "0.9",
        7: "0.9",
        8: "0.9",
        9: "0.9",
        12: "0.9",
        13: "0.9",
        14: "0.9",
        17: "0.9",
        21: "0.9",
        23: "0.9",
        24: "0.9",
        25: "0.9",
        26: "0.9",
        27: "0.9",
        28: "0.9",
        29: "0.9",
        30: "0.9",
        31: "0.9",
        32: "0.9",
        33: "0.9",
        34: "0.9",
        38: "0.9",
    },
    "CpuModelPath": {
        0: "john_snow_labs_guideline_summarizer_for_asthma_breast_cancer.johnsnowlabs_folder.en_summarize_clinical_guidelines_large_pipeline_cpu",
        1: "john_snow_labs_extract_procedures_and_measurements_and_their_corresponding_cpt_codes.johnsnowlabs_folder.en_resolve_cpt_augmented_cpu",
        2: "john_snow_labs_extract_laboratory_observations_and_the_corresponding_loinc_codes.johnsnowlabs_folder.en_resolve_loinc_augmented_cpu",
        6: "john_snow_labs_extract_neurologic_deficits_related_to_stroke_scale_nihss.johnsnowlabs_folder.en_med_ner_nihss_pipeline_cpu",
        7: "john_snow_labs_extract_clinical_findings_and_the_corresponding_icd_9_codes.johnsnowlabs_folder.en_resolve_icd9_pipeline_cpu",
        8: "john_snow_labs_extract_phenotypic_abnormalities_and_the_coresponding_hpo_codes_.johnsnowlabs_folder.en_resolve_HPO_cpu",
        9: "john_snow_labs_extract_findings_in_radiology_reports.johnsnowlabs_folder.en_explain_doc_clinical_radiology_pipeline_cpu",
        12: "john_snow_labs_extract_clinical_events_and_find_temporal_relations_era.johnsnowlabs_folder.en_explain_doc_era_cpu",
        13: "john_snow_labs_detect_pathogen,_medical_condition_and_medicine.johnsnowlabs_folder.en_med_ner_pathogen_pipeline_cpu",  # TODO BAD!! also __!!!
        14: "john_snow_labs_resolve_oncology_terminology_with_icd_o_taxonomy.johnsnowlabs_folder.en_resolve_icdo_augmented_cpu",
        17: "john_snow_labs_extract_social_determinants_of_health.johnsnowlabs_folder.en_med_ner_sdoh_langtest_pipeline_cpu",
        21: "john_snow_labs_clinical_de_identification_for_portuguese_mask.johnsnowlabs_folder.pt_deid_clinical_cpu",
        23: "john_snow_labs_clinical_de_identification_mask.johnsnowlabs_folder.en_de_identify_clinical_pipeline_cpu",
        24: "john_snow_labs_clinical_de_identification_for_romanian_mask.johnsnowlabs_folder.ro_deid_clinical_cpu",
        25: "john_snow_labs_clinical_de_identification_for_french_mask.johnsnowlabs_folder.fr_deid_obfuscated_cpu",
        26: "john_snow_labs_clinical_de_identification_for_spanish_mask.johnsnowlabs_folder.es_deid_clinical_cpu",
        27: "john_snow_labs_snomed_codes_to_icdo_codes_mapper.johnsnowlabs_folder.en_map_entity_snomed_to_icdo_cpu",
        28: "john_snow_labs_extract_clinical_risk_factors.johnsnowlabs_folder.en_med_ner_risk_factors_pipeline_cpu",
        29: "john_snow_labs_clinical_de_identification_for_german_mask.johnsnowlabs_folder.de_deid_clinical_cpu",
        30: "john_snow_labs_clinical_de_identification_foritalian_mask.johnsnowlabs_folder.it_deid_clinical_cpu",
        31: "john_snow_labs_extract_adverse_drug_events_ade.johnsnowlabs_folder.en_explain_doc_clinical_ade_cpu",
        32: "john_snow_labs_summarize_radiology_reports.johnsnowlabs_folder.en_summarize_radiology_pipeline_cpu",
        33: "john_snow_labs_extract_living_species.johnsnowlabs_folder.en_med_ner_living_species_pipeline_cpu",
        34: "john_snow_labs_extract_anatomical_structures.johnsnowlabs_folder.en_med_ner_anatom_pipeline_cpu",
        38: "john_snow_labs_detect_cancer_genetics.johnsnowlabs_folder.en_med_ner_bionlp_pipeline_cpu",
    },
    "GpuModelPath": {
        0: "john_snow_labs_guideline_summarizer_for_asthma_breast_cancer.johnsnowlabs_folder.en_summarize_clinical_guidelines_large_pipeline_gpu",
        1: "john_snow_labs_extract_procedures_and_measurements_and_their_corresponding_cpt_codes.johnsnowlabs_folder.en_resolve_cpt_augmented_gpu",
        2: "john_snow_labs_extract_laboratory_observations_and_the_corresponding_loinc_codes.johnsnowlabs_folder.en_resolve_loinc_augmented_gpu",
        6: "john_snow_labs_extract_neurologic_deficits_related_to_stroke_scale_nihss.johnsnowlabs_folder.en_med_ner_nihss_pipeline_gpu",
        7: "john_snow_labs_extract_clinical_findings_and_the_corresponding_icd_9_codes.johnsnowlabs_folder.en_resolve_icd9_pipeline_gpu",
        8: "john_snow_labs_extract_phenotypic_abnormalities_and_the_coresponding_hpo_codes_.johnsnowlabs_folder.en_resolve_HPO_gpu",
        9: "john_snow_labs_extract_findings_in_radiology_reports.johnsnowlabs_folder.en_explain_doc_clinical_radiology_pipeline_gpu",
        12: "john_snow_labs_extract_clinical_events_and_find_temporal_relations_era.johnsnowlabs_folder.en_explain_doc_era_gpu",
        13: "john_snow_labs_detect_pathogen,_medical_condition_and_medicine.johnsnowlabs_folder.en_med_ner_pathogen_pipeline_gpu",
        14: "john_snow_labs_resolve_oncology_terminology_with_icd_o_taxonomy.johnsnowlabs_folder.en_resolve_icdo_augmented_gpu",
        17: "john_snow_labs_extract_social_determinants_of_health.johnsnowlabs_folder.en_med_ner_sdoh_langtest_pipeline_gpu",
        21: "john_snow_labs_clinical_de_identification_for_portuguese_mask.johnsnowlabs_folder.pt_deid_clinical_gpu",
        23: "john_snow_labs_clinical_de_identification_mask.johnsnowlabs_folder.en_de_identify_clinical_pipeline_gpu",
        24: "john_snow_labs_clinical_de_identification_for_romanian_mask.johnsnowlabs_folder.ro_deid_clinical_gpu",
        25: "john_snow_labs_clinical_de_identification_for_french_mask.johnsnowlabs_folder.fr_deid_obfuscated_gpu",
        26: "john_snow_labs_clinical_de_identification_for_spanish_mask.johnsnowlabs_folder.es_deid_clinical_gpu",
        27: "john_snow_labs_snomed_codes_to_icdo_codes_mapper.johnsnowlabs_folder.en_map_entity_snomed_to_icdo_gpu",
        28: "john_snow_labs_extract_clinical_risk_factors.johnsnowlabs_folder.en_med_ner_risk_factors_pipeline_gpu",
        29: "john_snow_labs_clinical_de_identification_for_german_mask.johnsnowlabs_folder.de_deid_clinical_gpu",
        30: "john_snow_labs_clinical_de_identification_foritalian_mask.johnsnowlabs_folder.it_deid_clinical_gpu",
        31: "john_snow_labs_extract_adverse_drug_events_ade.johnsnowlabs_folder.en_explain_doc_clinical_ade_gpu",
        32: "john_snow_labs_summarize_radiology_reports.johnsnowlabs_folder.en_summarize_radiology_pipeline_gpu",
        33: "john_snow_labs_extract_living_species.johnsnowlabs_folder.en_med_ner_living_species_pipeline_gpu",
        34: "john_snow_labs_extract_anatomical_structures.johnsnowlabs_folder.en_med_ner_anatom_pipeline_gpu",
        38: "john_snow_labs_detect_cancer_genetics.johnsnowlabs_folder.en_med_ner_bionlp_pipeline_gpu",
    },
    "ListingId": {
        0: "153b223a-d73f-479f-a51c-8905434b545d",
        1: "e1a5be5d-b799-4bd1-a664-c31b9c47225f",
        2: "a299884a-7a95-4ddf-96e0-b8594c4290d3",
        6: "7afe6ca0-ad66-489b-b2d0-b31b0644d053",
        7: "c2469843-c104-4201-9db5-ba1542823448",
        8: "d07d7654-d483-4f1d-bb26-13b02197b87f",
        9: "a516cbd4-107d-4194-ab02-74095c155f34",
        12: "2a078943-c56d-48b1-a99d-3addb38d688f",
        13: "f52c1b80-794f-457f-bb94-51c5df3ee4be",
        14: "074bbfa7-20ad-4444-8e0a-bc05ff07d6ea",
        17: "c23fe435-9461-4d0e-a829-d64f6fecb659",
        21: "a5111c18-1c60-4c02-a25a-fa709e819ecd",
        23: "40f9b4db-ba84-4af1-aba6-57abfba24676",
        24: "8a7ef1cd-c307-4bc7-94c7-4b812a64d3c4",
        25: "c600aad0-84c6-4f3d-ae92-5541d3cad171",
        26: "c0456a4c-beeb-4258-9b4a-12e0964e33e5",
        27: "e3d2930b-b3bc-4f26-9d35-e81fa9fdd161",
        28: "4d973f25-f457-4af7-8ea7-7c3fddaf9493",
        29: "833ccefd-89a0-4e74-8b1d-ddb32181693b",
        30: "51ec7304-2cce-4c60-830e-9fe735ac2a89",
        31: "64d6608b-8341-4b14-8edd-c1a1b31823a6",
        32: "0fa941ad-cf3d-4b03-8e46-854e6299afe8",
        33: "7418db61-8ff0-49db-ae87-756fc17382fc",
        34: "7487be7b-0f6d-4aaf-82ef-ea2b1833685a",
        38: "0a5aebb4-6f73-4af6-96d4-f8d2acfce25d",
    },
    "PrivateListingId": {
        0: "153b223a-d73f-479f-a51c-8905434b545d",
        1: "e1a5be5d-b799-4bd1-a664-c31b9c47225f",
        2: "a299884a-7a95-4ddf-96e0-b8594c4290d3",
        6: "7afe6ca0-ad66-489b-b2d0-b31b0644d053",
        7: "c2469843-c104-4201-9db5-ba1542823448",
        8: "d07d7654-d483-4f1d-bb26-13b02197b87f",
        9: "a516cbd4-107d-4194-ab02-74095c155f34",
        12: "2a078943-c56d-48b1-a99d-3addb38d688f",
        13: "f52c1b80-794f-457f-bb94-51c5df3ee4be",
        14: "074bbfa7-20ad-4444-8e0a-bc05ff07d6ea",
        17: "c23fe435-9461-4d0e-a829-d64f6fecb659",
        21: "a5111c18-1c60-4c02-a25a-fa709e819ecd",
        23: "40f9b4db-ba84-4af1-aba6-57abfba24676",
        24: "8a7ef1cd-c307-4bc7-94c7-4b812a64d3c4",
        25: "c600aad0-84c6-4f3d-ae92-5541d3cad171",
        26: "c0456a4c-beeb-4258-9b4a-12e0964e33e5",
        27: "e3d2930b-b3bc-4f26-9d35-e81fa9fdd161",
        28: "4d973f25-f457-4af7-8ea7-7c3fddaf9493",
        29: "833ccefd-89a0-4e74-8b1d-ddb32181693b",
        30: "51ec7304-2cce-4c60-830e-9fe735ac2a89",
        31: "64d6608b-8341-4b14-8edd-c1a1b31823a6",
        32: "0fa941ad-cf3d-4b03-8e46-854e6299afe8",
        33: "7418db61-8ff0-49db-ae87-756fc17382fc",
        34: "7487be7b-0f6d-4aaf-82ef-ea2b1833685a",
        38: "0a5aebb4-6f73-4af6-96d4-f8d2acfce25d",
    },
}

import pandas as pd

models_df = pd.DataFrame(models).reset_index()
models_df