import FilterExcelFile as fe
import DB_analysis as db

#path = r"old_files"

def create_data_day_0():
    day0 = [
            [{'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'KLVAMGIPESLR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 1.0, 'Protein Accessions': 156231067.0, '# Missed Cleavages': 1.0, 'Charge': 3.0, 'DeltaScore': 0.3661, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 438.59192, 'MH+ [Da]': 1313.7612, 'DeltaM [ppm]': 0.18, 'Deltam/z [Da]': 8e-05, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 65.2, 'RT [min]': 0.0099, 'First Scan': 3.0, 'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 1.12, 'Percolator q-Value': 0.7985, 'Percolator PEP': 0.9733},\
            {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'TmEQFTIHLTVNPQSK', 'Modifications': 'M2(Oxidation)', '# Protein Groups': 0.0, '# Proteins': 1.0, 'Protein Accessions': 156119625.0, '# Missed Cleavages': 0.0, 'Charge': 3.0, 'DeltaScore': 0.1967, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 630.65247, 'MH+ [Da]': 1889.94284, 'DeltaM [ppm]': 0.14, 'Deltam/z [Da]': 9e-05, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 65.2, 'RT [min]': 0.0111, 'First Scan': 4.0, 'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 0.61, 'Percolator q-Value': 0.5092, 'Percolator PEP': 0.8485},\
            {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'SYScQVTHEGSTVEK', 'Modifications': 'C4(Carbamidomethyl)', '# Protein Groups': 0.0, '# Proteins': 2.0, 'Protein Accessions': '239752152; 295986608', '# Missed Cleavages': 0.0, 'Charge': 3.0, 'DeltaScore': 0.549, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 571.25775, 'MH+ [Da]': 1711.7587, 'DeltaM [ppm]': -0.29, 'Deltam/z [Da]': -0.00016, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 65.2, 'RT [min]': 0.0124, 'First Scan': 5.0, 'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 1.53, 'Percolator q-Value': 0.07411, 'Percolator PEP': 0.3869},\
            {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'EEPEPLSPELEYIPR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 2.0, 'Protein Accessions': '116642887; 116642885', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': 0.2951, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 899.45074, 'MH+ [Da]': 1797.89421, 'DeltaM [ppm]': 2.05, 'Deltam/z [Da]': 0.00185, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 55.69253, 'Ion Inject Time [ms]': 65.2, 'RT [min]': 0.0136, 'First Scan': 6.0, 'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 0.61, 'Percolator q-Value': 0.9282, 'Percolator PEP': 0.9067},\
            {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'TSEPDFTSANMRDSAEGPK', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 2.0, 'Protein Accessions': '20336260; 20336258', '# Missed Cleavages': 1.0, 'Charge': 3.0, 'DeltaScore': 0.1964, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 680.63757, 'MH+ [Da]': 2039.89817, 'DeltaM [ppm]': 0.34, 'Deltam/z [Da]': 0.00023, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 65.2, 'RT [min]': 0.0148, 'First Scan': 7.0, 'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 0.46, 'Percolator q-Value': 0.8601, 'Percolator PEP': 0.9902},\
            {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'EEPEPLSPELEYIPR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 1.0, 'Protein Accessions': 239752604.0, '# Missed Cleavages': 1.0, 'Charge': 3.0, 'DeltaScore': 0.2393, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 635.65161, 'MH+ [Da]': 1904.94028, 'DeltaM [ppm]': -1.03, 'Deltam/z [Da]': -0.00065, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 12.83167, 'Ion Inject Time [ms]': 35.0, 'RT [min]': 0.0195, 'First Scan': 9.0, 'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 1.17, 'Percolator q-Value': 0.3904, 'Percolator PEP': 0.7657},\
            {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'NQSGATTSSGDTESEEGEGETTVRLLWLSMLKMPR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 1.0, 'Protein Accessions': 122937259.0, '# Missed Cleavages': 2.0, 'Charge': 4.0, 'DeltaScore': 0.069, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 950.20392, 'MH+ [Da]': 3797.79384, 'DeltaM [ppm]': -0.48, 'Deltam/z [Da]': -0.00045, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 41.62, 'RT [min]': 0.0202, 'First Scan': 10.0, 'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 0.5, 'Percolator q-Value': 0.9607, 'Percolator PEP': 1.0},\
            ],

            [{'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'TPEVTcVVVDVSHEDPEVQFNWYVDGMEVHNAK', 'Modifications': 'C6(Carbamidomethyl)', '# Protein Groups': 0.0, '# Proteins': 1.0, 'Protein Accessions': 239752604.0, '# Missed Cleavages': 0.0, 'Charge': 4.0, 'DeltaScore': 0.7067, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 958.19208, 'MH+ [Da]': 3829.74648, 'DeltaM [ppm]': -0.2, 'Deltam/z [Da]': -0.00019, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.5467755, 'Ion Inject Time [ms]': 40.068, 'RT [min]': 115.1234, 'First Scan': 96605.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 7.91, 'Percolator q-Value': 0.0, 'Percolator PEP': 3.264734e-08},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'ATLVcLISDFYPGAVTVAWK', 'Modifications': 'C5(Carbamidomethyl)', '# Protein Groups': 0.0, '# Proteins': 2.0, 'Protein Accessions': '239752152; 295986608', '# Missed Cleavages': 0.0, 'Charge': 3.0, 'DeltaScore': 0.5381, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 737.72247, 'MH+ [Da]': 2211.15287, 'DeltaM [ppm]': 0.46, 'Deltam/z [Da]': 0.00034, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 8.097445, 'Ion Inject Time [ms]': 35.0, 'RT [min]': 100.848, 'First Scan': 86381.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 0.39, 'Percolator q-Value': 0.0, 'Percolator PEP': 4.383e-07},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous', 'Annotated Sequence': 'QVELVESGGGLVQPGGSLR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 7.0, 'Protein Accessions': 'IBD001_3448138 chain: IGH M; IBD001_3251432 chain: IGH G; IBD001_2879280 chain: IGH M; IBD001_2796061 chain: IGH M; IBD001_3367715 chain: IGH M; IBD001_3268584 chain: IGH M; IBD001_2850991 chain: IGH M', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': 0.0036, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 941.50482, 'MH+ [Da]': 1882.00237, 'DeltaM [ppm]': -0.26, 'Deltam/z [Da]': -0.00025, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 3.246262, 'Ion Inject Time [ms]': 38.5, 'RT [min]': 52.7775, 'First Scan': 39574.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 5.55, 'Percolator q-Value': 9.0, 'Percolator PEP': 6.727e-07},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous', 'Annotated Sequence': 'EVQLVESGGGIVQPGGSLR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 250.0, 'Protein Accessions': 'IBD001_2616814 chain: IGH M; IBD001_2620927 chain: IGH M; IBD001_13525 chain: IGH G; IBD001_1282 chain: IGH G; IBD001_9259 chain: IGH M; IBD001_2629586 chain: IGH M; IBD001_2628919 chain: IGH M; IBD001_14052 chain: IGH G; IBD001_20059 chain: IGH G; IBD001_7580 chain: IGH M; IBD001_2624305 chain: IGH M; IBD001_6567 chain: IGH G; IBD001_3457 chain: IGH M; IBD001_20845 chain: IGH M; IBD001_14042 chain: IGH M; IBD001_11126 chain: IGH M; IBD001_2632503 chain: IGH M; IBD001_2625870 chain: IGH M; IBD001_14102 chain: IGH M; IBD001_12543 chain: IGH G; IBD001_2616594 chain: IGH M; IBD001_7662 chain: IGH G; IBD001_1751 chain: IGH unknown; IBD001_5371 chain: IGH G; IBD001_12660 chain: IGH G; IBD001_3706 chain: IGH A2; IBD001_5902 chain: IGH M; IBD001_19872 chain: IGH G; IBD001_2620615 chain: IGH M; IBD001_1057 chain: IGH G; IBD001_21106 chain: IGH M; IBD001_9305 chain: IGH G; IBD001_2628333 chain: IGH M; IBD001_14387 chain: IGH G; IBD001_2619618 chain: IGH M; IBD001_8329 chain: IGH G; IBD001_14876 chain: IGH M; IBD001_2623648 chain: IGH M; IBD001_2627937 chain: IGH M; IBD001_8731 chain: IGH A1; IBD001_2621953 chain: IGH M; IBD001_2618003 chain: IGH M; IBD001_1972 chain: IGH G; IBD001_2634233 chain: IGH M; IBD001_145011 chain: IGH M; IBD001_2624645 chain: IGH M; IBD001_2327 chain: IGH M; IBD001_12984 chain: IGH A1; IBD001_2629212 chain: IGH M; IBD001_2634241 chain: IGH M; IBD001_11508 chain: IGH unknown; IBD001_17547 chain: IGH G; IBD001_91 chain: IGH G; IBD001_2631736 chain: IGH G; IBD001_7875 chain: IGH G; IBD001_14742 chain: IGH M; IBD001_19484 chain: IGH G; IBD001_2630747 chain: IGH M; IBD001_3061 chain: IGH A1; IBD001_144901 chain: IGH G; IBD001_10950 chain: IGH A1; IBD001_5452 chain: IGH G; IBD001_10693 chain: IGH G; IBD001_11114 chain: IGH G; IBD001_9380 chain: IGH G; IBD001_17722 chain: IGH M; IBD001_4020 chain: IGH A1; IBD001_15880 chain: IGH G; IBD001_14397 chain: IGH M; IBD001_10500 chain: IGH G; IBD001_29 chain: IGH M; IBD001_12990 chain: IGH M; IBD001_2634468 chain: IGH M; IBD001_2626100 chain: IGH M; IBD001_2627893 chain: IGH M; IBD001_7641 chain: IGH M; IBD001_6448 chain: IGH G; IBD001_13498 chain: IGH G; IBD001_2633152 chain: IGH M; IBD001_93 chain: IGH G; IBD001_2622796 chain: IGH M; IBD001_14695 chain: IGH A1; IBD001_6777 chain: IGH M; IBD001_16832 chain: IGH G; IBD001_9544 chain: IGH G; IBD001_2628603 chain: IGH M; IBD001_2618373 chain: IGH M; IBD001_2633399 chain: IGH M; IBD001_21406 chain: IGH M; IBD001_2627558 chain: IGH M; IBD001_18735 chain: IGH G; IBD001_14131 chain: IGH M; IBD001_2617497 chain: IGH M; IBD001_2629838 chain: IGH M; IBD001_8334 chain: IGH A2; IBD001_2628280 chain: IGH M; IBD001_2617533 chain: IGH M; IBD001_8761 chain: IGH G; IBD001_17012 chain: IGH M; IBD001_16728 chain: IGH G; IBD001_2621534 chain: IGH M; IBD001_2624159 chain: IGH M; IBD001_2624205 chain: IGH M; IBD001_2630137 chain: IGH M; IBD001_2629525 chain: IGH M; IBD001_13750 chain: IGH G; IBD001_19855 chain: IGH G; IBD001_17051 chain: IGH A2; IBD001_18640 chain: IGH M; IBD001_2628815 chain: IGH M; IBD001_2262 chain: IGH M; IBD001_20431 chain: IGH unknown; IBD001_5260 chain: IGH M; IBD001_15403 chain: IGH G; IBD001_2626848 chain: IGH M; IBD001_2632193 chain: IGH M; IBD001_2618087 chain: IGH M; IBD001_15685 chain: IGH A1; IBD001_857 chain: IGH G; IBD001_2623130 chain: IGH G; IBD001_2618495 chain: IGH M; IBD001_12793 chain: IGH G; IBD001_2624786 chain: IGH M; IBD001_2620568 chain: IGH M; IBD001_2633522 chain: IGH M; IBD001_17349 chain: IGH M; IBD001_8772 chain: IGH G; IBD001_10719 chain: IGH G; IBD001_2632610 chain: IGH M; IBD001_20706 chain: IGH G; IBD001_2634422 chain: IGH M; IBD001_2623565 chain: IGH M; IBD001_2624942 chain: IGH M; IBD001_16886 chain: IGH M; IBD001_2632751 chain: IGH M; IBD001_3665 chain: IGH M; IBD001_2629871 chain: IGH M; IBD001_2616516 chain: IGH M; IBD001_4694 chain: IGH M; IBD001_2617368 chain: IGH M; IBD001_12239 chain: IGH M; IBD001_3623 chain: IGH G; IBD001_2633945 chain: IGH M; IBD001_3401 chain: IGH M; IBD001_2632352 chain: IGH M; IBD001_2627375 chain: IGH M; IBD001_4949 chain: IGH M; IBD001_14256 chain: IGH M; IBD001_2633646 chain: IGH M; IBD001_816 chain: IGH M; IBD001_184 chain: IGH G; IBD001_8598 chain: IGH M; IBD001_16585 chain: IGH G; IBD001_7686 chain: IGH M; IBD001_3356 chain: IGH G; IBD001_2632571 chain: IGH M; IBD001_2629142 chain: IGH M; IBD001_2633908 chain: IGH M; IBD001_1139 chain: IGH M; IBD001_2620961 chain: IGH G; IBD001_1625 chain: IGH A1; IBD001_11313 chain: IGH G; IBD001_3824 chain: IGH M; IBD001_21031 chain: IGH G; IBD001_1199 chain: IGH G; IBD001_2167 chain: IGH G; IBD001_33 chain: IGH G; IBD001_5815 chain: IGH G; IBD001_2633103 chain: IGH M; IBD001_16771 chain: IGH M; IBD001_15435 chain: IGH G; IBD001_2627477 chain: IGH M; IBD001_12602 chain: IGH M; IBD001_2626032 chain: IGH M; IBD001_2617754 chain: IGH M; IBD001_12448 chain: IGH G; IBD001_5970 chain: IGH G; IBD001_12625 chain: IGH A1; IBD001_144619 chain: IGH M; IBD001_21424 chain: IGH G; IBD001_20825 chain: IGH G; IBD001_16474 chain: IGH M; IBD001_15593 chain: IGH G; IBD001_2619118 chain: IGH M; IBD001_15285 chain: IGH G; IBD001_2629501 chain: IGH M; IBD001_3007 chain: IGH G; IBD001_11155 chain: IGH G; IBD001_2625513 chain: IGH M; IBD001_2635317 chain: IGH M; IBD001_7347 chain: IGH M; IBD001_2631296 chain: IGH M; IBD001_2631516 chain: IGH M; IBD001_1219 chain: IGH M; IBD001_19669 chain: IGH G; IBD001_4711 chain: IGH G; IBD001_9443 chain: IGH M; IBD001_2631057 chain: IGH M; IBD001_2632142 chain: IGH M; IBD001_21094 chain: IGH M; IBD001_4215 chain: IGH M; IBD001_3821 chain: IGH M; IBD001_2627811 chain: IGH M; IBD001_2620967 chain: IGH M; IBD001_2631824 chain: IGH M; IBD001_2626368 chain: IGH M; IBD001_7805 chain: IGH M; IBD001_2622871 chain: IGH M; IBD001_2633215 chain: IGH M; IBD001_17936 chain: IGH M; IBD001_15287 chain: IGH G; IBD001_17020 chain: IGH G; IBD001_21041 chain: IGH M; IBD001_9176 chain: IGH M; IBD001_18127 chain: IGH G; IBD001_2630516 chain: IGH M; IBD001_15135 chain: IGH M; IBD001_2634956 chain: IGH M; IBD001_576 chain: IGH M; IBD001_2632802 chain: IGH M; IBD001_14957 chain: IGH G; IBD001_5587 chain: IGH A1; IBD001_15949 chain: IGH A2; IBD001_5301 chain: IGH G; IBD001_2634751 chain: IGH M; IBD001_2626440 chain: IGH M; IBD001_13838 chain: IGH G; IBD001_2629205 chain: IGH M; IBD001_2632668 chain: IGH M; IBD001_6716 chain: IGH G; IBD001_9859 chain: IGH M; IBD001_19588 chain: IGH M; IBD001_18383 chain: IGH M; IBD001_5466 chain: IGH M; IBD001_19963 chain: IGH M; IBD001_5224 chain: IGH M; IBD001_2634205 chain: IGH M; IBD001_2626501 chain: IGH M; IBD001_18544 chain: IGH G; IBD001_9031 chain: IGH G; IBD001_2631313 chain: IGH M; IBD001_2633219 chain: IGH M; IBD001_19757 chain: IGH G; IBD001_2631343 chain: IGH M; IBD001_2627899 chain: IGH M; IBD001_2467 chain: IGH G; IBD001_9195 chain: IGH M; IBD001_2633422 chain: IGH M; IBD001_2632694 chain: IGH M; IBD001_12013 chain: IGH M', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': 0.0245, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 948.51337, 'MH+ [Da]': 1896.01946, 'DeltaM [ppm]': 0.5, 'Deltam/z [Da]': 0.00047, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 6.615, 'RT [min]': 63.9353, 'First Scan': 49578.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 6.13, 'Percolator q-Value': 0.0, 'Percolator PEP': 1.014},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'ATLVcLISDFYPGAVTVAWK', 'Modifications': 'C5(Carbamidomethyl)', '# Protein Groups': 0.0, '# Proteins': 2.0, 'Protein Accessions': '239752152; 295986608', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': 0.6252, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 1106.07996, 'MH+ [Da]': 2211.15264, 'DeltaM [ppm]': 0.36, 'Deltam/z [Da]': 0.0004, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 5.267097, 'Ion Inject Time [ms]': 21.205, 'RT [min]': 99.8256, 'First Scan': 85369.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 0.41, 'Percolator q-Value': 0.0, 'Percolator PEP': 1.289e-06},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous', 'Annotated Sequence': 'EVQLVESGGGIVQPGGSLR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 1.0, 'Protein Accessions': 'IBD001_2865383 chain: IGH M', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': '', 'DeltaCn': 0.0036, 'Rank': 2.0, 'Search Engine Rank': 2.0, 'm/z [Da]': 941.50482, 'MH+ [Da]': 1882.00237, 'DeltaM [ppm]': -0.26, 'Deltam/z [Da]': -0.00025, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 3.246262, 'Ion Inject Time [ms]': 38.5, 'RT [min]': 52.7775, 'First Scan': 39574.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 0.53, 'Percolator q-Value': 0.0, 'Percolator PEP': 1.672e-06},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous', 'Annotated Sequence': 'EVQLVESGGGLVQPGGSLR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 250.0, 'Protein Accessions': 'IBD001_5832 chain: IGH unknown; IBD001_11805 chain: IGH M; IBD001_4443 chain: IGH G; IBD001_4503 chain: IGH G; IBD001_5763 chain: IGH A2; IBD001_13942 chain: IGH M; IBD001_12860 chain: IGH G; IBD001_7695 chain: IGH M; IBD001_13689 chain: IGH M; IBD001_13727 chain: IGH G; IBD001_15234 chain: IGH M; IBD001_15102 chain: IGH A1; IBD001_6829 chain: IGH G; IBD001_9742 chain: IGH G; IBD001_7708 chain: IGH G; IBD001_11645 chain: IGH M; IBD001_13676 chain: IGH M; IBD001_10773 chain: IGH M; IBD001_15225 chain: IGH G; IBD001_6753 chain: IGH G; IBD001_4379 chain: IGH M; IBD001_15568 chain: IGH G; IBD001_4826 chain: IGH A1; IBD001_13744 chain: IGH M; IBD001_16451 chain: IGH G; IBD001_2772 chain: IGH M; IBD001_13785 chain: IGH G; IBD001_14917 chain: IGH M; IBD001_6737 chain: IGH M; IBD001_6683 chain: IGH M; IBD001_6858 chain: IGH G; IBD001_6358 chain: IGH G; IBD001_5866 chain: IGH M; IBD001_5272 chain: IGH G; IBD001_5490 chain: IGH M; IBD001_15650 chain: IGH A1; IBD001_12688 chain: IGH A; IBD001_6861 chain: IGH M; IBD001_6136 chain: IGH G; IBD001_15472 chain: IGH M; IBD001_179 chain: IGH G; IBD001_11654 chain: IGH G; IBD001_5649 chain: IGH G; IBD001_7878 chain: IGH M; IBD001_1816 chain: IGH G; IBD001_14966 chain: IGH M; IBD001_11860 chain: IGH A1; IBD001_15913 chain: IGH G; IBD001_84 chain: IGH G; IBD001_669 chain: IGH G; IBD001_15095 chain: IGH G; IBD001_11569 chain: IGH M; IBD001_2629 chain: IGH M; IBD001_7059 chain: IGH M; IBD001_14245 chain: IGH M; IBD001_10875 chain: IGH M; IBD001_9993 chain: IGH A1; IBD001_9905 chain: IGH G; IBD001_1347 chain: IGH M; IBD001_1842 chain: IGH M; IBD001_13563 chain: IGH G; IBD001_5908 chain: IGH M; IBD001_16748 chain: IGH G; IBD001_13773 chain: IGH G; IBD001_2635 chain: IGH G; IBD001_6919 chain: IGH G; IBD001_12658 chain: IGH G; IBD001_15142 chain: IGH M; IBD001_15869 chain: IGH M; IBD001_2674 chain: IGH G; IBD001_14335 chain: IGH unknown; IBD001_6987 chain: IGH G; IBD001_8647 chain: IGH M; IBD001_2779 chain: IGH M; IBD001_9611 chain: IGH G; IBD001_10537 chain: IGH G; IBD001_15494 chain: IGH G; IBD001_5948 chain: IGH G; IBD001_10709 chain: IGH M; IBD001_8900 chain: IGH G; IBD001_13752 chain: IGH M; IBD001_4621 chain: IGH G; IBD001_12352 chain: IGH M; IBD001_10209 chain: IGH G; IBD001_16760 chain: IGH M; IBD001_15585 chain: IGH M; IBD001_12662 chain: IGH G; IBD001_9781 chain: IGH G; IBD001_13020 chain: IGH M; IBD001_653 chain: IGH A1; IBD001_14851 chain: IGH G; IBD001_8762 chain: IGH G; IBD001_14455 chain: IGH G; IBD001_6508 chain: IGH G; IBD001_16599 chain: IGH G; IBD001_7653 chain: IGH G; IBD001_16297 chain: IGH M; IBD001_13678 chain: IGH G; IBD001_13205 chain: IGH M; IBD001_3016 chain: IGH G; IBD001_6666 chain: IGH M; IBD001_16298 chain: IGH G; IBD001_7260 chain: IGH G; IBD001_7941 chain: IGH G; IBD001_13884 chain: IGH G; IBD001_11093 chain: IGH M; IBD001_10211 chain: IGH A1; IBD001_12501 chain: IGH M; IBD001_847 chain: IGH G; IBD001_6939 chain: IGH M; IBD001_3683 chain: IGH A; IBD001_4529 chain: IGH G; IBD001_7119 chain: IGH G; IBD001_16770 chain: IGH M; IBD001_14948 chain: IGH M; IBD001_1887 chain: IGH unknown; IBD001_5373 chain: IGH unknown; IBD001_10723 chain: IGH M; IBD001_11157 chain: IGH M; IBD001_1228 chain: IGH M; IBD001_16272 chain: IGH M; IBD001_10045 chain: IGH G; IBD001_2723 chain: IGH G; IBD001_4061 chain: IGH M; IBD001_13625 chain: IGH A1; IBD001_3887 chain: IGH G; IBD001_6123 chain: IGH M; IBD001_5220 chain: IGH unknown; IBD001_10168 chain: IGH G; IBD001_1691 chain: IGH G; IBD001_11198 chain: IGH M; IBD001_2797 chain: IGH M; IBD001_16369 chain: IGH M; IBD001_12114 chain: IGH A1; IBD001_14726 chain: IGH G; IBD001_15446 chain: IGH M; IBD001_9621 chain: IGH M; IBD001_3837 chain: IGH M; IBD001_7681 chain: IGH G; IBD001_5281 chain: IGH G; IBD001_14046 chain: IGH A1; IBD001_10580 chain: IGH G; IBD001_3357 chain: IGH G; IBD001_8619 chain: IGH G; IBD001_10521 chain: IGH G; IBD001_6659 chain: IGH G; IBD001_3218 chain: IGH G; IBD001_5138 chain: IGH M; IBD001_3928 chain: IGH G; IBD001_11791 chain: IGH M; IBD001_13982 chain: IGH unknown; IBD001_3193 chain: IGH M; IBD001_6107 chain: IGH M; IBD001_3327 chain: IGH A2; IBD001_10410 chain: IGH G; IBD001_16532 chain: IGH A1; IBD001_3722 chain: IGH G; IBD001_11968 chain: IGH M; IBD001_6022 chain: IGH G; IBD001_7457 chain: IGH G; IBD001_12408 chain: IGH M; IBD001_6625 chain: IGH M; IBD001_7441 chain: IGH M; IBD001_5576 chain: IGH G; IBD001_3704 chain: IGH M; IBD001_15414 chain: IGH M; IBD001_10730 chain: IGH G; IBD001_5508 chain: IGH G; IBD001_759 chain: IGH G; IBD001_7779 chain: IGH G; IBD001_1703 chain: IGH M; IBD001_12097 chain: IGH A1; IBD001_1745 chain: IGH M; IBD001_11055 chain: IGH G; IBD001_11015 chain: IGH G; IBD001_9796 chain: IGH A2; IBD001_14631 chain: IGH M; IBD001_16277 chain: IGH M; IBD001_8840 chain: IGH M; IBD001_13940 chain: IGH M; IBD001_6550 chain: IGH G; IBD001_9872 chain: IGH G; IBD001_12734 chain: IGH G; IBD001_5244 chain: IGH M; IBD001_10790 chain: IGH M; IBD001_3235 chain: IGH M; IBD001_13900 chain: IGH G; IBD001_13643 chain: IGH G; IBD001_1973 chain: IGH M; IBD001_5536 chain: IGH M; IBD001_4000 chain: IGH M; IBD001_14 chain: IGH M; IBD001_3617 chain: IGH M; IBD001_16424 chain: IGH G; IBD001_8373 chain: IGH G; IBD001_15553 chain: IGH G; IBD001_15530 chain: IGH M; IBD001_16208 chain: IGH G; IBD001_8929 chain: IGH G; IBD001_16428 chain: IGH G; IBD001_16112 chain: IGH A1; IBD001_9788 chain: IGH G; IBD001_9432 chain: IGH G; IBD001_13050 chain: IGH M; IBD001_11984 chain: IGH M; IBD001_7574 chain: IGH A1; IBD001_14272 chain: IGH G; IBD001_2540 chain: IGH M; IBD001_16285 chain: IGH M; IBD001_13496 chain: IGH A1; IBD001_7685 chain: IGH M; IBD001_12723 chain: IGH G; IBD001_9247 chain: IGH G; IBD001_1027 chain: IGH G; IBD001_13063 chain: IGH A1; IBD001_9709 chain: IGH G; IBD001_14608 chain: IGH G; IBD001_5077 chain: IGH G; IBD001_9691 chain: IGH M; IBD001_15841 chain: IGH A2; IBD001_9272 chain: IGH A2; IBD001_899 chain: IGH M; IBD001_1570 chain: IGH G; IBD001_14227 chain: IGH G; IBD001_12710 chain: IGH G; IBD001_14473 chain: IGH G; IBD001_10953 chain: IGH M; IBD001_15160 chain: IGH M; IBD001_15825 chain: IGH G; IBD001_12241 chain: IGH M; IBD001_11399 chain: IGH M; IBD001_8769 chain: IGH M; IBD001_3571 chain: IGH M; IBD001_5914 chain: IGH M; IBD001_8549 chain: IGH M; IBD001_11698 chain: IGH M; IBD001_11124 chain: IGH M; IBD001_11925 chain: IGH G; IBD001_6923 chain: IGH A1; IBD001_8829 chain: IGH A2; IBD001_8224 chain: IGH G; IBD001_11559 chain: IGH G; IBD001_3479 chain: IGH M; IBD001_14288 chain: IGH M; IBD001_4248 chain: IGH G; IBD001_6386 chain: IGH M; IBD001_1864 chain: IGH M; IBD001_5880 chain: IGH M; IBD001_13780 chain: IGH G; IBD001_3436 chain: IGH M', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': '', 'DeltaCn': 0.0036, 'Rank': 2.0, 'Search Engine Rank': 3.0, 'm/z [Da]': 941.50482, 'MH+ [Da]': 1882.00237, 'DeltaM [ppm]': -0.26, 'Deltam/z [Da]': -0.00025, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 3.246262, 'Ion Inject Time [ms]': 38.5, 'RT [min]': 52.7775, 'First Scan': 39574.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 5.53, 'Percolator q-Value': 10.0, 'Percolator PEP': 1.672e-06},\
            ],

            [{'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'ATLVcLISDFYPGAVTVAWK', 'Modifications': 'C7(Carbamidomethyl)', '# Protein Groups': 0.0, '# Proteins': 1.0, 'Protein Accessions': 239752604.0, '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': 0.433, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 581.31879, 'MH+ [Da]': 1161.6303, 'DeltaM [ppm]': 0.58, 'Deltam/z [Da]': 0.00034, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 5.802906, 'Ion Inject Time [ms]': 186.7, 'RT [min]': 0.0098, 'First Scan': 3.0, 'Spectrum File': '6597_JL_3c.raw', 'Ions Matched': '0/0', 'XCorr': 2.24, 'Percolator q-Value': 0.001378, 'Percolator PEP': 0.03863},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous', 'Annotated Sequence': 'EEPEPLSPELEYIPR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 5.0, 'Protein Accessions': 'IBD001_2304707 chain: IGK; IBD001_2156652 chain: IGK; IBD001_2365509 chain: IGK; IBD001_1064749 chain: IGK; IBD001_1924658 chain: IGK', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': '', 'DeltaCn': 0.0229, 'Rank': 5.0, 'Search Engine Rank': 5.0, 'm/z [Da]': 929.48346, 'MH+ [Da]': 1857.95964, 'DeltaM [ppm]': 2.37, 'Deltam/z [Da]': 0.0022, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 44.819, 'RT [min]': 50.5905, 'First Scan': 37337.0, 'Spectrum File': '6597_JL_3c.raw', 'Ions Matched': '0/0', 'XCorr': 2.56, 'Percolator q-Value': 0.001833, 'Percolator PEP': 1.04681},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous', 'Annotated Sequence': 'DTVLTQSPATLSVSPGER', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 6.0, 'Protein Accessions': 'IBD001_2228630 chain: IGK; IBD001_1569545 chain: IGK; IBD001_1084794 chain: IGK; IBD001_194334 chain: IGK; IBD001_1608875 chain: IGK; IBD001_1280818 chain: IGK', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': '', 'DeltaCn': 0.0344, 'Rank': 6.0, 'Search Engine Rank': 6.0, 'm/z [Da]': 929.48346, 'MH+ [Da]': 1857.95964, 'DeltaM [ppm]': 2.37, 'Deltam/z [Da]': 0.0022, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 44.819, 'RT [min]': 50.5905, 'First Scan': 37337.0, 'Spectrum File': '6597_JL_3c.raw', 'Ions Matched': '0/0', 'XCorr': 2.53, 'Percolator q-Value': 0.004188, 'Percolator PEP': 0.1253},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'ASQGIGSALAWYQQKPGEAPK', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 4.0, 'Protein Accessions': 'IBD001_3639067 chain: IGK; IBD001_3199771 chain: IGK; IBD001_3146599 chain: IGK; IBD001_3134161 chain: IGK', '# Missed Cleavages': 0.0, 'Charge': 3.0, 'DeltaScore': 0.3041, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 729.71082, 'MH+ [Da]': 2187.11789, 'DeltaM [ppm]': -0.64, 'Deltam/z [Da]': -0.00047, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 20.56961, 'Ion Inject Time [ms]': 31.9, 'RT [min]': 50.6307, 'First Scan': 37372.0, 'Spectrum File': '6597_JL_3c.raw', 'Ions Matched': '0/0', 'XCorr': 0.396, 'Percolator q-Value': 0.001833, 'Percolator PEP': 0.04849},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous', 'Annotated Sequence': 'ASQGIGSALAWYQQKPGEAPK', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 4.0, 'Protein Accessions': 'IBD001_3639067 chain: IGK; IBD001_3199771 chain: IGK; IBD001_3146599 chain: IGK; IBD001_3134161 chain: IGK', '# Missed Cleavages': 0.0, 'Charge': 3.0, 'DeltaScore': 0.3041, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 729.71082, 'MH+ [Da]': 2187.11789, 'DeltaM [ppm]': -0.64, 'Deltam/z [Da]': -0.00047, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 20.56961, 'Ion Inject Time [ms]': 31.9, 'RT [min]': 50.6307, 'First Scan': 37372.0, 'Spectrum File': '6597_JL_3c.raw', 'Ions Matched': '0/0', 'XCorr': 0.96, 'Percolator q-Value': 0.001833, 'Percolator PEP': 0.04849},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous', 'Annotated Sequence': 'EEPEPLSPELEYIPR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 17.0, 'Protein Accessions': 'IBD001_331249 chain: IGK; IBD001_1600821 chain: IGK; IBD001_3514663 chain: IGK; IBD001_1201634 chain: IGK; IBD001_1230126 chain: IGK; IBD001_85151 chain: IGK; IBD001_3639067 chain: IGK; IBD001_1753128 chain: IGK; IBD001_624134 chain: IGK; IBD001_3146599 chain: IGK; IBD001_572144 chain: IGK; IBD001_3134161 chain: IGK; IBD001_1394427 chain: IGK; IBD001_420687 chain: IGK; IBD001_1201865 chain: IGK; IBD001_2126963 chain: IGK; IBD001_1449447 chain: IGK', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': 0.0095, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 815.44427, 'MH+ [Da]': 1629.88127, 'DeltaM [ppm]': 0.4, 'Deltam/z [Da]': 0.00032, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 48.75179, 'Ion Inject Time [ms]': 38.655, 'RT [min]': 50.7173, 'First Scan': 37457.0, 'Spectrum File': '6597_JL_3c.raw', 'Ions Matched': '0/0', 'XCorr': 3.17, 'Percolator q-Value': 0.0, 'Percolator PEP': 0.999},\
            {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous', 'Annotated Sequence': 'SYScQVTHEGSTVEK', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 2.0, 'Protein Accessions': 'IBD001_3211847 chain: IGK; IBD001_1954018 chain: IGK', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': '', 'DeltaCn': 0.0095, 'Rank': 2.0, 'Search Engine Rank': 2.0, 'm/z [Da]': 815.44427, 'MH+ [Da]': 1629.88127, 'DeltaM [ppm]': 0.4, 'Deltam/z [Da]': 0.00032, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 48.75179, 'Ion Inject Time [ms]': 38.655, 'RT [min]': 50.7173, 'First Scan': 37457.0, 'Spectrum File': '6597_JL_3c.raw', 'Ions Matched': '0/0', 'XCorr': 0.14, 'Percolator q-Value': 0.0, 'Percolator PEP': 0.00292},\
            ]
        ]
    return day0


def create_data_day_10():
    day10 = [
        [{'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'KLG', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 1.0,
          'Protein Accessions': 156231067.0, '# Missed Cleavages': 1.0, 'Charge': 3.0, 'DeltaScore': 0.3661,
          'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 438.59192, 'MH+ [Da]': 1313.7612,
          'DeltaM [ppm]': 0.18, 'Deltam/z [Da]': 8e-05, 'Activation Type': 'CID', 'MS Order': 'MS2',
          'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 65.2, 'RT [min]': 0.0099, 'First Scan': 3.0,
          'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 1.12, 'Percolator q-Value': 0.7985,
          'Percolator PEP': 0.9733}, \
         {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'TmEQFTIHLTVNPQSK', 'Modifications': 'M2(Oxidation)', '# Protein Groups': 0.0,
          '# Proteins': 1.0, 'Protein Accessions': 156119625.0, '# Missed Cleavages': 0.0, 'Charge': 3.0,
          'DeltaScore': 0.1967, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 630.65247,
          'MH+ [Da]': 1889.94284, 'DeltaM [ppm]': 0.14, 'Deltam/z [Da]': 9e-05, 'Activation Type': 'CID',
          'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 65.2, 'RT [min]': 0.0111,
          'First Scan': 4.0, 'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 0.61,
          'Percolator q-Value': 0.5092, 'Percolator PEP': 0.8485}, \
         {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'SYe', 'Modifications': 'C4(Carbamidomethyl)', '# Protein Groups': 0.0,
          '# Proteins': 2.0, 'Protein Accessions': '239752152; 295986608', '# Missed Cleavages': 0.0, 'Charge': 3.0,
          'DeltaScore': 0.549, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 571.25775,
          'MH+ [Da]': 1711.7587, 'DeltaM [ppm]': -0.29, 'Deltam/z [Da]': -0.00016, 'Activation Type': 'CID',
          'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 65.2, 'RT [min]': 0.0124,
          'First Scan': 5.0, 'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 1.53,
          'Percolator q-Value': 0.07411, 'Percolator PEP': 0.3869}, \
         {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'EEPEPLSPELEYIPR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 2.0,
          'Protein Accessions': '116642887; 116642885', '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': 0.2951,
          'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 899.45074, 'MH+ [Da]': 1797.89421,
          'DeltaM [ppm]': 2.05, 'Deltam/z [Da]': 0.00185, 'Activation Type': 'CID', 'MS Order': 'MS2',
          'Isolation Interference [%]': 55.69253, 'Ion Inject Time [ms]': 65.2, 'RT [min]': 0.0136, 'First Scan': 6.0,
          'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 0.61, 'Percolator q-Value': 0.9282,
          'Percolator PEP': 0.9067}, \
         {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'TSqPDFTSANMRDSAEGPK', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 2.0,
          'Protein Accessions': '20336260; 20336258', '# Missed Cleavages': 1.0, 'Charge': 3.0, 'DeltaScore': 0.1964,
          'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 680.63757, 'MH+ [Da]': 2039.89817,
          'DeltaM [ppm]': 0.34, 'Deltam/z [Da]': 0.00023, 'Activation Type': 'CID', 'MS Order': 'MS2',
          'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 65.2, 'RT [min]': 0.0148, 'First Scan': 7.0,
          'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 0.46, 'Percolator q-Value': 0.8601,
          'Percolator PEP': 0.9902}, \
         {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'EEmEPLSPmLEYIPR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 1.0,
          'Protein Accessions': 239752604.0, '# Missed Cleavages': 1.0, 'Charge': 3.0, 'DeltaScore': 0.2393,
          'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 635.65161, 'MH+ [Da]': 1904.94028,
          'DeltaM [ppm]': -1.03, 'Deltam/z [Da]': -0.00065, 'Activation Type': 'CID', 'MS Order': 'MS2',
          'Isolation Interference [%]': 12.83167, 'Ion Inject Time [ms]': 35.0, 'RT [min]': 0.0195, 'First Scan': 9.0,
          'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 1.17, 'Percolator q-Value': 0.3904,
          'Percolator PEP': 0.7657}, \
         {'Checked': 1, 'Confidence': 'Low', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'NQSGATTSSGDTESEEGEGETTVRLLWLSMLKMPR', 'Modifications': '', '# Protein Groups': 0.0,
          '# Proteins': 1.0, 'Protein Accessions': 122937259.0, '# Missed Cleavages': 2.0, 'Charge': 4.0,
          'DeltaScore': 0.069, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 950.20392,
          'MH+ [Da]': 3797.79384, 'DeltaM [ppm]': -0.48, 'Deltam/z [Da]': -0.00045, 'Activation Type': 'CID',
          'MS Order': 'MS2', 'Isolation Interference [%]': 0.0, 'Ion Inject Time [ms]': 41.62, 'RT [min]': 0.0202,
          'First Scan': 10.0, 'Spectrum File': '6597_JL_3a.raw', 'Ions Matched': '0/0', 'XCorr': 0.5,
          'Percolator q-Value': 0.9607, 'Percolator PEP': 1.0}, \
         ],

        [{'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'TPEVTcVVVDVSHEDPEVQFNWYVDGMEVHNAK', 'Modifications': 'C6(Carbamidomethyl)',
          '# Protein Groups': 0.0, '# Proteins': 1.0, 'Protein Accessions': 239752604.0, '# Missed Cleavages': 0.0,
          'Charge': 4.0, 'DeltaScore': 0.7067, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0,
          'm/z [Da]': 958.19208, 'MH+ [Da]': 3829.74648, 'DeltaM [ppm]': -0.2, 'Deltam/z [Da]': -0.00019,
          'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.5467755,
          'Ion Inject Time [ms]': 40.068, 'RT [min]': 115.1234, 'First Scan': 96605.0,
          'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 7.91, 'Percolator q-Value': 0.0,
          'Percolator PEP': 3.264734e-08}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'AToVcLISDFYPGAVTVAWK', 'Modifications': 'C5(Carbamidomethyl)', '# Protein Groups': 0.0,
          '# Proteins': 2.0, 'Protein Accessions': '239752152; 295986608', '# Missed Cleavages': 0.0, 'Charge': 3.0,
          'DeltaScore': 0.5381, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 737.72247,
          'MH+ [Da]': 2211.15287, 'DeltaM [ppm]': 0.46, 'Deltam/z [Da]': 0.00034, 'Activation Type': 'CID',
          'MS Order': 'MS2', 'Isolation Interference [%]': 8.097445, 'Ion Inject Time [ms]': 35.0, 'RT [min]': 100.848,
          'First Scan': 86381.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 0.39,
          'Percolator q-Value': 0.0, 'Percolator PEP': 4.383e-07}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous',
          'Annotated Sequence': 'QVaLVESGGGLVQPGGSLR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 7.0,
          'Protein Accessions': 'IBD001_3448138 chain: IGH M; IBD001_3251432 chain: IGH G; IBD001_2879280 chain: IGH M; IBD001_2796061 chain: IGH M; IBD001_3367715 chain: IGH M; IBD001_3268584 chain: IGH M; IBD001_2850991 chain: IGH M',
          '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': 0.0036, 'DeltaCn': 0.0, 'Rank': 1.0,
          'Search Engine Rank': 1.0, 'm/z [Da]': 941.50482, 'MH+ [Da]': 1882.00237, 'DeltaM [ppm]': -0.26,
          'Deltam/z [Da]': -0.00025, 'Activation Type': 'CID', 'MS Order': 'MS2',
          'Isolation Interference [%]': 3.246262, 'Ion Inject Time [ms]': 38.5, 'RT [min]': 52.7775,
          'First Scan': 39574.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 5.55,
          'Percolator q-Value': 9.0, 'Percolator PEP': 6.727e-07}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous',
          'Annotated Sequence': 'EVzLVESGGGIVQPGGSLR', 'Modifications': '', '# Protein Groups': 0.0,
          '# Proteins': 250.0,
          'Protein Accessions': 'IBD001_2616814 chain: IGH M; IBD001_2620927 chain: IGH M; IBD001_13525 chain: IGH G; IBD001_1282 chain: IGH G; IBD001_9259 chain: IGH M; IBD001_2629586 chain: IGH M; IBD001_2628919 chain: IGH M; IBD001_14052 chain: IGH G; IBD001_20059 chain: IGH G; IBD001_7580 chain: IGH M; IBD001_2624305 chain: IGH M; IBD001_6567 chain: IGH G; IBD001_3457 chain: IGH M; IBD001_20845 chain: IGH M; IBD001_14042 chain: IGH M; IBD001_11126 chain: IGH M; IBD001_2632503 chain: IGH M; IBD001_2625870 chain: IGH M; IBD001_14102 chain: IGH M; IBD001_12543 chain: IGH G; IBD001_2616594 chain: IGH M; IBD001_7662 chain: IGH G; IBD001_1751 chain: IGH unknown; IBD001_5371 chain: IGH G; IBD001_12660 chain: IGH G; IBD001_3706 chain: IGH A2; IBD001_5902 chain: IGH M; IBD001_19872 chain: IGH G; IBD001_2620615 chain: IGH M; IBD001_1057 chain: IGH G; IBD001_21106 chain: IGH M; IBD001_9305 chain: IGH G; IBD001_2628333 chain: IGH M; IBD001_14387 chain: IGH G; IBD001_2619618 chain: IGH M; IBD001_8329 chain: IGH G; IBD001_14876 chain: IGH M; IBD001_2623648 chain: IGH M; IBD001_2627937 chain: IGH M; IBD001_8731 chain: IGH A1; IBD001_2621953 chain: IGH M; IBD001_2618003 chain: IGH M; IBD001_1972 chain: IGH G; IBD001_2634233 chain: IGH M; IBD001_145011 chain: IGH M; IBD001_2624645 chain: IGH M; IBD001_2327 chain: IGH M; IBD001_12984 chain: IGH A1; IBD001_2629212 chain: IGH M; IBD001_2634241 chain: IGH M; IBD001_11508 chain: IGH unknown; IBD001_17547 chain: IGH G; IBD001_91 chain: IGH G; IBD001_2631736 chain: IGH G; IBD001_7875 chain: IGH G; IBD001_14742 chain: IGH M; IBD001_19484 chain: IGH G; IBD001_2630747 chain: IGH M; IBD001_3061 chain: IGH A1; IBD001_144901 chain: IGH G; IBD001_10950 chain: IGH A1; IBD001_5452 chain: IGH G; IBD001_10693 chain: IGH G; IBD001_11114 chain: IGH G; IBD001_9380 chain: IGH G; IBD001_17722 chain: IGH M; IBD001_4020 chain: IGH A1; IBD001_15880 chain: IGH G; IBD001_14397 chain: IGH M; IBD001_10500 chain: IGH G; IBD001_29 chain: IGH M; IBD001_12990 chain: IGH M; IBD001_2634468 chain: IGH M; IBD001_2626100 chain: IGH M; IBD001_2627893 chain: IGH M; IBD001_7641 chain: IGH M; IBD001_6448 chain: IGH G; IBD001_13498 chain: IGH G; IBD001_2633152 chain: IGH M; IBD001_93 chain: IGH G; IBD001_2622796 chain: IGH M; IBD001_14695 chain: IGH A1; IBD001_6777 chain: IGH M; IBD001_16832 chain: IGH G; IBD001_9544 chain: IGH G; IBD001_2628603 chain: IGH M; IBD001_2618373 chain: IGH M; IBD001_2633399 chain: IGH M; IBD001_21406 chain: IGH M; IBD001_2627558 chain: IGH M; IBD001_18735 chain: IGH G; IBD001_14131 chain: IGH M; IBD001_2617497 chain: IGH M; IBD001_2629838 chain: IGH M; IBD001_8334 chain: IGH A2; IBD001_2628280 chain: IGH M; IBD001_2617533 chain: IGH M; IBD001_8761 chain: IGH G; IBD001_17012 chain: IGH M; IBD001_16728 chain: IGH G; IBD001_2621534 chain: IGH M; IBD001_2624159 chain: IGH M; IBD001_2624205 chain: IGH M; IBD001_2630137 chain: IGH M; IBD001_2629525 chain: IGH M; IBD001_13750 chain: IGH G; IBD001_19855 chain: IGH G; IBD001_17051 chain: IGH A2; IBD001_18640 chain: IGH M; IBD001_2628815 chain: IGH M; IBD001_2262 chain: IGH M; IBD001_20431 chain: IGH unknown; IBD001_5260 chain: IGH M; IBD001_15403 chain: IGH G; IBD001_2626848 chain: IGH M; IBD001_2632193 chain: IGH M; IBD001_2618087 chain: IGH M; IBD001_15685 chain: IGH A1; IBD001_857 chain: IGH G; IBD001_2623130 chain: IGH G; IBD001_2618495 chain: IGH M; IBD001_12793 chain: IGH G; IBD001_2624786 chain: IGH M; IBD001_2620568 chain: IGH M; IBD001_2633522 chain: IGH M; IBD001_17349 chain: IGH M; IBD001_8772 chain: IGH G; IBD001_10719 chain: IGH G; IBD001_2632610 chain: IGH M; IBD001_20706 chain: IGH G; IBD001_2634422 chain: IGH M; IBD001_2623565 chain: IGH M; IBD001_2624942 chain: IGH M; IBD001_16886 chain: IGH M; IBD001_2632751 chain: IGH M; IBD001_3665 chain: IGH M; IBD001_2629871 chain: IGH M; IBD001_2616516 chain: IGH M; IBD001_4694 chain: IGH M; IBD001_2617368 chain: IGH M; IBD001_12239 chain: IGH M; IBD001_3623 chain: IGH G; IBD001_2633945 chain: IGH M; IBD001_3401 chain: IGH M; IBD001_2632352 chain: IGH M; IBD001_2627375 chain: IGH M; IBD001_4949 chain: IGH M; IBD001_14256 chain: IGH M; IBD001_2633646 chain: IGH M; IBD001_816 chain: IGH M; IBD001_184 chain: IGH G; IBD001_8598 chain: IGH M; IBD001_16585 chain: IGH G; IBD001_7686 chain: IGH M; IBD001_3356 chain: IGH G; IBD001_2632571 chain: IGH M; IBD001_2629142 chain: IGH M; IBD001_2633908 chain: IGH M; IBD001_1139 chain: IGH M; IBD001_2620961 chain: IGH G; IBD001_1625 chain: IGH A1; IBD001_11313 chain: IGH G; IBD001_3824 chain: IGH M; IBD001_21031 chain: IGH G; IBD001_1199 chain: IGH G; IBD001_2167 chain: IGH G; IBD001_33 chain: IGH G; IBD001_5815 chain: IGH G; IBD001_2633103 chain: IGH M; IBD001_16771 chain: IGH M; IBD001_15435 chain: IGH G; IBD001_2627477 chain: IGH M; IBD001_12602 chain: IGH M; IBD001_2626032 chain: IGH M; IBD001_2617754 chain: IGH M; IBD001_12448 chain: IGH G; IBD001_5970 chain: IGH G; IBD001_12625 chain: IGH A1; IBD001_144619 chain: IGH M; IBD001_21424 chain: IGH G; IBD001_20825 chain: IGH G; IBD001_16474 chain: IGH M; IBD001_15593 chain: IGH G; IBD001_2619118 chain: IGH M; IBD001_15285 chain: IGH G; IBD001_2629501 chain: IGH M; IBD001_3007 chain: IGH G; IBD001_11155 chain: IGH G; IBD001_2625513 chain: IGH M; IBD001_2635317 chain: IGH M; IBD001_7347 chain: IGH M; IBD001_2631296 chain: IGH M; IBD001_2631516 chain: IGH M; IBD001_1219 chain: IGH M; IBD001_19669 chain: IGH G; IBD001_4711 chain: IGH G; IBD001_9443 chain: IGH M; IBD001_2631057 chain: IGH M; IBD001_2632142 chain: IGH M; IBD001_21094 chain: IGH M; IBD001_4215 chain: IGH M; IBD001_3821 chain: IGH M; IBD001_2627811 chain: IGH M; IBD001_2620967 chain: IGH M; IBD001_2631824 chain: IGH M; IBD001_2626368 chain: IGH M; IBD001_7805 chain: IGH M; IBD001_2622871 chain: IGH M; IBD001_2633215 chain: IGH M; IBD001_17936 chain: IGH M; IBD001_15287 chain: IGH G; IBD001_17020 chain: IGH G; IBD001_21041 chain: IGH M; IBD001_9176 chain: IGH M; IBD001_18127 chain: IGH G; IBD001_2630516 chain: IGH M; IBD001_15135 chain: IGH M; IBD001_2634956 chain: IGH M; IBD001_576 chain: IGH M; IBD001_2632802 chain: IGH M; IBD001_14957 chain: IGH G; IBD001_5587 chain: IGH A1; IBD001_15949 chain: IGH A2; IBD001_5301 chain: IGH G; IBD001_2634751 chain: IGH M; IBD001_2626440 chain: IGH M; IBD001_13838 chain: IGH G; IBD001_2629205 chain: IGH M; IBD001_2632668 chain: IGH M; IBD001_6716 chain: IGH G; IBD001_9859 chain: IGH M; IBD001_19588 chain: IGH M; IBD001_18383 chain: IGH M; IBD001_5466 chain: IGH M; IBD001_19963 chain: IGH M; IBD001_5224 chain: IGH M; IBD001_2634205 chain: IGH M; IBD001_2626501 chain: IGH M; IBD001_18544 chain: IGH G; IBD001_9031 chain: IGH G; IBD001_2631313 chain: IGH M; IBD001_2633219 chain: IGH M; IBD001_19757 chain: IGH G; IBD001_2631343 chain: IGH M; IBD001_2627899 chain: IGH M; IBD001_2467 chain: IGH G; IBD001_9195 chain: IGH M; IBD001_2633422 chain: IGH M; IBD001_2632694 chain: IGH M; IBD001_12013 chain: IGH M',
          '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': 0.0245, 'DeltaCn': 0.0, 'Rank': 1.0,
          'Search Engine Rank': 1.0, 'm/z [Da]': 948.51337, 'MH+ [Da]': 1896.01946, 'DeltaM [ppm]': 0.5,
          'Deltam/z [Da]': 0.00047, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0,
          'Ion Inject Time [ms]': 6.615, 'RT [min]': 63.9353, 'First Scan': 49578.0, 'Spectrum File': '6597_JL_3b.raw',
          'Ions Matched': '0/0', 'XCorr': 6.13, 'Percolator q-Value': 0.0, 'Percolator PEP': 1.014}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'ATLVcLISDFYPGAVTVAWK', 'Modifications': 'C5(Carbamidomethyl)', '# Protein Groups': 0.0,
          '# Proteins': 2.0, 'Protein Accessions': '239752152; 295986608', '# Missed Cleavages': 0.0, 'Charge': 2.0,
          'DeltaScore': 0.6252, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 1106.07996,
          'MH+ [Da]': 2211.15264, 'DeltaM [ppm]': 0.36, 'Deltam/z [Da]': 0.0004, 'Activation Type': 'CID',
          'MS Order': 'MS2', 'Isolation Interference [%]': 5.267097, 'Ion Inject Time [ms]': 21.205,
          'RT [min]': 99.8256, 'First Scan': 85369.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0',
          'XCorr': 0.41, 'Percolator q-Value': 0.0, 'Percolator PEP': 1.289e-06}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous',
          'Annotated Sequence': 'EVQLVESGGGIVQPGGSLR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 1.0,
          'Protein Accessions': 'IBD001_2865383 chain: IGH M', '# Missed Cleavages': 0.0, 'Charge': 2.0,
          'DeltaScore': '', 'DeltaCn': 0.0036, 'Rank': 2.0, 'Search Engine Rank': 2.0, 'm/z [Da]': 941.50482,
          'MH+ [Da]': 1882.00237, 'DeltaM [ppm]': -0.26, 'Deltam/z [Da]': -0.00025, 'Activation Type': 'CID',
          'MS Order': 'MS2', 'Isolation Interference [%]': 3.246262, 'Ion Inject Time [ms]': 38.5, 'RT [min]': 52.7775,
          'First Scan': 39574.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 0.53,
          'Percolator q-Value': 0.0, 'Percolator PEP': 1.672e-06}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous',
          'Annotated Sequence': 'EVQLVESGGGLVQPGGSLR', 'Modifications': '', '# Protein Groups': 0.0,
          '# Proteins': 250.0,
          'Protein Accessions': 'IBD001_5832 chain: IGH unknown; IBD001_11805 chain: IGH M; IBD001_4443 chain: IGH G; IBD001_4503 chain: IGH G; IBD001_5763 chain: IGH A2; IBD001_13942 chain: IGH M; IBD001_12860 chain: IGH G; IBD001_7695 chain: IGH M; IBD001_13689 chain: IGH M; IBD001_13727 chain: IGH G; IBD001_15234 chain: IGH M; IBD001_15102 chain: IGH A1; IBD001_6829 chain: IGH G; IBD001_9742 chain: IGH G; IBD001_7708 chain: IGH G; IBD001_11645 chain: IGH M; IBD001_13676 chain: IGH M; IBD001_10773 chain: IGH M; IBD001_15225 chain: IGH G; IBD001_6753 chain: IGH G; IBD001_4379 chain: IGH M; IBD001_15568 chain: IGH G; IBD001_4826 chain: IGH A1; IBD001_13744 chain: IGH M; IBD001_16451 chain: IGH G; IBD001_2772 chain: IGH M; IBD001_13785 chain: IGH G; IBD001_14917 chain: IGH M; IBD001_6737 chain: IGH M; IBD001_6683 chain: IGH M; IBD001_6858 chain: IGH G; IBD001_6358 chain: IGH G; IBD001_5866 chain: IGH M; IBD001_5272 chain: IGH G; IBD001_5490 chain: IGH M; IBD001_15650 chain: IGH A1; IBD001_12688 chain: IGH A; IBD001_6861 chain: IGH M; IBD001_6136 chain: IGH G; IBD001_15472 chain: IGH M; IBD001_179 chain: IGH G; IBD001_11654 chain: IGH G; IBD001_5649 chain: IGH G; IBD001_7878 chain: IGH M; IBD001_1816 chain: IGH G; IBD001_14966 chain: IGH M; IBD001_11860 chain: IGH A1; IBD001_15913 chain: IGH G; IBD001_84 chain: IGH G; IBD001_669 chain: IGH G; IBD001_15095 chain: IGH G; IBD001_11569 chain: IGH M; IBD001_2629 chain: IGH M; IBD001_7059 chain: IGH M; IBD001_14245 chain: IGH M; IBD001_10875 chain: IGH M; IBD001_9993 chain: IGH A1; IBD001_9905 chain: IGH G; IBD001_1347 chain: IGH M; IBD001_1842 chain: IGH M; IBD001_13563 chain: IGH G; IBD001_5908 chain: IGH M; IBD001_16748 chain: IGH G; IBD001_13773 chain: IGH G; IBD001_2635 chain: IGH G; IBD001_6919 chain: IGH G; IBD001_12658 chain: IGH G; IBD001_15142 chain: IGH M; IBD001_15869 chain: IGH M; IBD001_2674 chain: IGH G; IBD001_14335 chain: IGH unknown; IBD001_6987 chain: IGH G; IBD001_8647 chain: IGH M; IBD001_2779 chain: IGH M; IBD001_9611 chain: IGH G; IBD001_10537 chain: IGH G; IBD001_15494 chain: IGH G; IBD001_5948 chain: IGH G; IBD001_10709 chain: IGH M; IBD001_8900 chain: IGH G; IBD001_13752 chain: IGH M; IBD001_4621 chain: IGH G; IBD001_12352 chain: IGH M; IBD001_10209 chain: IGH G; IBD001_16760 chain: IGH M; IBD001_15585 chain: IGH M; IBD001_12662 chain: IGH G; IBD001_9781 chain: IGH G; IBD001_13020 chain: IGH M; IBD001_653 chain: IGH A1; IBD001_14851 chain: IGH G; IBD001_8762 chain: IGH G; IBD001_14455 chain: IGH G; IBD001_6508 chain: IGH G; IBD001_16599 chain: IGH G; IBD001_7653 chain: IGH G; IBD001_16297 chain: IGH M; IBD001_13678 chain: IGH G; IBD001_13205 chain: IGH M; IBD001_3016 chain: IGH G; IBD001_6666 chain: IGH M; IBD001_16298 chain: IGH G; IBD001_7260 chain: IGH G; IBD001_7941 chain: IGH G; IBD001_13884 chain: IGH G; IBD001_11093 chain: IGH M; IBD001_10211 chain: IGH A1; IBD001_12501 chain: IGH M; IBD001_847 chain: IGH G; IBD001_6939 chain: IGH M; IBD001_3683 chain: IGH A; IBD001_4529 chain: IGH G; IBD001_7119 chain: IGH G; IBD001_16770 chain: IGH M; IBD001_14948 chain: IGH M; IBD001_1887 chain: IGH unknown; IBD001_5373 chain: IGH unknown; IBD001_10723 chain: IGH M; IBD001_11157 chain: IGH M; IBD001_1228 chain: IGH M; IBD001_16272 chain: IGH M; IBD001_10045 chain: IGH G; IBD001_2723 chain: IGH G; IBD001_4061 chain: IGH M; IBD001_13625 chain: IGH A1; IBD001_3887 chain: IGH G; IBD001_6123 chain: IGH M; IBD001_5220 chain: IGH unknown; IBD001_10168 chain: IGH G; IBD001_1691 chain: IGH G; IBD001_11198 chain: IGH M; IBD001_2797 chain: IGH M; IBD001_16369 chain: IGH M; IBD001_12114 chain: IGH A1; IBD001_14726 chain: IGH G; IBD001_15446 chain: IGH M; IBD001_9621 chain: IGH M; IBD001_3837 chain: IGH M; IBD001_7681 chain: IGH G; IBD001_5281 chain: IGH G; IBD001_14046 chain: IGH A1; IBD001_10580 chain: IGH G; IBD001_3357 chain: IGH G; IBD001_8619 chain: IGH G; IBD001_10521 chain: IGH G; IBD001_6659 chain: IGH G; IBD001_3218 chain: IGH G; IBD001_5138 chain: IGH M; IBD001_3928 chain: IGH G; IBD001_11791 chain: IGH M; IBD001_13982 chain: IGH unknown; IBD001_3193 chain: IGH M; IBD001_6107 chain: IGH M; IBD001_3327 chain: IGH A2; IBD001_10410 chain: IGH G; IBD001_16532 chain: IGH A1; IBD001_3722 chain: IGH G; IBD001_11968 chain: IGH M; IBD001_6022 chain: IGH G; IBD001_7457 chain: IGH G; IBD001_12408 chain: IGH M; IBD001_6625 chain: IGH M; IBD001_7441 chain: IGH M; IBD001_5576 chain: IGH G; IBD001_3704 chain: IGH M; IBD001_15414 chain: IGH M; IBD001_10730 chain: IGH G; IBD001_5508 chain: IGH G; IBD001_759 chain: IGH G; IBD001_7779 chain: IGH G; IBD001_1703 chain: IGH M; IBD001_12097 chain: IGH A1; IBD001_1745 chain: IGH M; IBD001_11055 chain: IGH G; IBD001_11015 chain: IGH G; IBD001_9796 chain: IGH A2; IBD001_14631 chain: IGH M; IBD001_16277 chain: IGH M; IBD001_8840 chain: IGH M; IBD001_13940 chain: IGH M; IBD001_6550 chain: IGH G; IBD001_9872 chain: IGH G; IBD001_12734 chain: IGH G; IBD001_5244 chain: IGH M; IBD001_10790 chain: IGH M; IBD001_3235 chain: IGH M; IBD001_13900 chain: IGH G; IBD001_13643 chain: IGH G; IBD001_1973 chain: IGH M; IBD001_5536 chain: IGH M; IBD001_4000 chain: IGH M; IBD001_14 chain: IGH M; IBD001_3617 chain: IGH M; IBD001_16424 chain: IGH G; IBD001_8373 chain: IGH G; IBD001_15553 chain: IGH G; IBD001_15530 chain: IGH M; IBD001_16208 chain: IGH G; IBD001_8929 chain: IGH G; IBD001_16428 chain: IGH G; IBD001_16112 chain: IGH A1; IBD001_9788 chain: IGH G; IBD001_9432 chain: IGH G; IBD001_13050 chain: IGH M; IBD001_11984 chain: IGH M; IBD001_7574 chain: IGH A1; IBD001_14272 chain: IGH G; IBD001_2540 chain: IGH M; IBD001_16285 chain: IGH M; IBD001_13496 chain: IGH A1; IBD001_7685 chain: IGH M; IBD001_12723 chain: IGH G; IBD001_9247 chain: IGH G; IBD001_1027 chain: IGH G; IBD001_13063 chain: IGH A1; IBD001_9709 chain: IGH G; IBD001_14608 chain: IGH G; IBD001_5077 chain: IGH G; IBD001_9691 chain: IGH M; IBD001_15841 chain: IGH A2; IBD001_9272 chain: IGH A2; IBD001_899 chain: IGH M; IBD001_1570 chain: IGH G; IBD001_14227 chain: IGH G; IBD001_12710 chain: IGH G; IBD001_14473 chain: IGH G; IBD001_10953 chain: IGH M; IBD001_15160 chain: IGH M; IBD001_15825 chain: IGH G; IBD001_12241 chain: IGH M; IBD001_11399 chain: IGH M; IBD001_8769 chain: IGH M; IBD001_3571 chain: IGH M; IBD001_5914 chain: IGH M; IBD001_8549 chain: IGH M; IBD001_11698 chain: IGH M; IBD001_11124 chain: IGH M; IBD001_11925 chain: IGH G; IBD001_6923 chain: IGH A1; IBD001_8829 chain: IGH A2; IBD001_8224 chain: IGH G; IBD001_11559 chain: IGH G; IBD001_3479 chain: IGH M; IBD001_14288 chain: IGH M; IBD001_4248 chain: IGH G; IBD001_6386 chain: IGH M; IBD001_1864 chain: IGH M; IBD001_5880 chain: IGH M; IBD001_13780 chain: IGH G; IBD001_3436 chain: IGH M',
          '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': '', 'DeltaCn': 0.0036, 'Rank': 2.0,
          'Search Engine Rank': 3.0, 'm/z [Da]': 941.50482, 'MH+ [Da]': 1882.00237, 'DeltaM [ppm]': -0.26,
          'Deltam/z [Da]': -0.00025, 'Activation Type': 'CID', 'MS Order': 'MS2',
          'Isolation Interference [%]': 3.246262, 'Ion Inject Time [ms]': 38.5, 'RT [min]': 52.7775,
          'First Scan': 39574.0, 'Spectrum File': '6597_JL_3b.raw', 'Ions Matched': '0/0', 'XCorr': 5.53,
          'Percolator q-Value': 10.0, 'Percolator PEP': 1.672e-06}, \
         ],

        [{'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'ATLVcLISDFYPGAVTVAWK', 'Modifications': 'C7(Carbamidomethyl)', '# Protein Groups': 0.0,
          '# Proteins': 1.0, 'Protein Accessions': 239752604.0, '# Missed Cleavages': 0.0, 'Charge': 2.0,
          'DeltaScore': 0.433, 'DeltaCn': 0.0, 'Rank': 1.0, 'Search Engine Rank': 1.0, 'm/z [Da]': 581.31879,
          'MH+ [Da]': 1161.6303, 'DeltaM [ppm]': 0.58, 'Deltam/z [Da]': 0.00034, 'Activation Type': 'CID',
          'MS Order': 'MS2', 'Isolation Interference [%]': 5.802906, 'Ion Inject Time [ms]': 186.7, 'RT [min]': 0.0098,
          'First Scan': 3.0, 'Spectrum File': '6597_JL_3c.raw', 'Ions Matched': '0/0', 'XCorr': 2.24,
          'Percolator q-Value': 0.001378, 'Percolator PEP': 0.03863}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous',
          'Annotated Sequence': 'EEwEPLSPELEYIPR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 5.0,
          'Protein Accessions': 'IBD001_2304707 chain: IGK; IBD001_2156652 chain: IGK; IBD001_2365509 chain: IGK; IBD001_1064749 chain: IGK; IBD001_1924658 chain: IGK',
          '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': '', 'DeltaCn': 0.0229, 'Rank': 5.0,
          'Search Engine Rank': 5.0, 'm/z [Da]': 929.48346, 'MH+ [Da]': 1857.95964, 'DeltaM [ppm]': 2.37,
          'Deltam/z [Da]': 0.0022, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0,
          'Ion Inject Time [ms]': 44.819, 'RT [min]': 50.5905, 'First Scan': 37337.0, 'Spectrum File': '6597_JL_3c.raw',
          'Ions Matched': '0/0', 'XCorr': 2.56, 'Percolator q-Value': 0.001833, 'Percolator PEP': 1.04681}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous',
          'Annotated Sequence': 'DTVLTQSPATLSVSPGER', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 6.0,
          'Protein Accessions': 'IBD001_2228630 chain: IGK; IBD001_1569545 chain: IGK; IBD001_1084794 chain: IGK; IBD001_194334 chain: IGK; IBD001_1608875 chain: IGK; IBD001_1280818 chain: IGK',
          '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': '', 'DeltaCn': 0.0344, 'Rank': 6.0,
          'Search Engine Rank': 6.0, 'm/z [Da]': 929.48346, 'MH+ [Da]': 1857.95964, 'DeltaM [ppm]': 2.37,
          'Deltam/z [Da]': 0.0022, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 0.0,
          'Ion Inject Time [ms]': 44.819, 'RT [min]': 50.5905, 'First Scan': 37337.0, 'Spectrum File': '6597_JL_3c.raw',
          'Ions Matched': '0/0', 'XCorr': 2.53, 'Percolator q-Value': 0.004188, 'Percolator PEP': 0.1253}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'ASQGIGSALAWYQQKPGEAPK', 'Modifications': '', '# Protein Groups': 0.0,
          '# Proteins': 4.0,
          'Protein Accessions': 'IBD001_3639067 chain: IGK; IBD001_3199771 chain: IGK; IBD001_3146599 chain: IGK; IBD001_3134161 chain: IGK',
          '# Missed Cleavages': 0.0, 'Charge': 3.0, 'DeltaScore': 0.3041, 'DeltaCn': 0.0, 'Rank': 1.0,
          'Search Engine Rank': 1.0, 'm/z [Da]': 729.71082, 'MH+ [Da]': 2187.11789, 'DeltaM [ppm]': -0.64,
          'Deltam/z [Da]': -0.00047, 'Activation Type': 'CID', 'MS Order': 'MS2',
          'Isolation Interference [%]': 20.56961, 'Ion Inject Time [ms]': 31.9, 'RT [min]': 50.6307,
          'First Scan': 37372.0, 'Spectrum File': '6597_JL_3c.raw', 'Ions Matched': '0/0', 'XCorr': 0.396,
          'Percolator q-Value': 0.001833, 'Percolator PEP': 0.04849}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Unambiguous',
          'Annotated Sequence': 'TSEPDFTSANMRDSAEGPK', 'Modifications': '', '# Protein Groups': 0.0,
          '# Proteins': 4.0,
          'Protein Accessions': 'IBD001_3639067 chain: IGK; IBD001_3199771 chain: IGK; IBD001_3146599 chain: IGK; IBD001_3134161 chain: IGK',
          '# Missed Cleavages': 0.0, 'Charge': 3.0, 'DeltaScore': 0.3041, 'DeltaCn': 0.0, 'Rank': 1.0,
          'Search Engine Rank': 1.0, 'm/z [Da]': 729.71082, 'MH+ [Da]': 2187.11789, 'DeltaM [ppm]': -0.64,
          'Deltam/z [Da]': -0.00047, 'Activation Type': 'CID', 'MS Order': 'MS2',
          'Isolation Interference [%]': 20.56961, 'Ion Inject Time [ms]': 31.9, 'RT [min]': 50.6307,
          'First Scan': 37372.0, 'Spectrum File': '6597_JL_3c.raw', 'Ions Matched': '0/0', 'XCorr': 0.96,
          'Percolator q-Value': 0.001833, 'Percolator PEP': 0.04849}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous',
          'Annotated Sequence': 'EEPEPLSPELEYIPR', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 17.0,
          'Protein Accessions': 'IBD001_331249 chain: IGK; IBD001_1600821 chain: IGK; IBD001_3514663 chain: IGK; IBD001_1201634 chain: IGK; IBD001_1230126 chain: IGK; IBD001_85151 chain: IGK; IBD001_3639067 chain: IGK; IBD001_1753128 chain: IGK; IBD001_624134 chain: IGK; IBD001_3146599 chain: IGK; IBD001_572144 chain: IGK; IBD001_3134161 chain: IGK; IBD001_1394427 chain: IGK; IBD001_420687 chain: IGK; IBD001_1201865 chain: IGK; IBD001_2126963 chain: IGK; IBD001_1449447 chain: IGK',
          '# Missed Cleavages': 0.0, 'Charge': 2.0, 'DeltaScore': 0.0095, 'DeltaCn': 0.0, 'Rank': 1.0,
          'Search Engine Rank': 1.0, 'm/z [Da]': 815.44427, 'MH+ [Da]': 1629.88127, 'DeltaM [ppm]': 0.4,
          'Deltam/z [Da]': 0.00032, 'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 48.75179,
          'Ion Inject Time [ms]': 38.655, 'RT [min]': 50.7173, 'First Scan': 37457.0, 'Spectrum File': '6597_JL_3c.raw',
          'Ions Matched': '0/0', 'XCorr': 3.17, 'Percolator q-Value': 0.0, 'Percolator PEP': 0.999}, \
         {'Checked': 1, 'Confidence': 'High', 'Identifying Node': 'Sequest HT (A7)', 'PSM Ambiguity': 'Ambiguous',
          'Annotated Sequence': 'SYScQVTHEGSTVEK', 'Modifications': '', '# Protein Groups': 0.0, '# Proteins': 2.0,
          'Protein Accessions': 'IBD001_3211847 chain: IGK; IBD001_1954018 chain: IGK', '# Missed Cleavages': 0.0,
          'Charge': 2.0, 'DeltaScore': '', 'DeltaCn': 0.0095, 'Rank': 2.0, 'Search Engine Rank': 2.0,
          'm/z [Da]': 815.44427, 'MH+ [Da]': 1629.88127, 'DeltaM [ppm]': 0.4, 'Deltam/z [Da]': 0.00032,
          'Activation Type': 'CID', 'MS Order': 'MS2', 'Isolation Interference [%]': 48.75179,
          'Ion Inject Time [ms]': 38.655, 'RT [min]': 50.7173, 'First Scan': 37457.0, 'Spectrum File': '6597_JL_3c.raw',
          'Ions Matched': '0/0', 'XCorr': 0.14, 'Percolator q-Value': 0.0, 'Percolator PEP': 0.00292}, \
         ]
    ]
    return day10


def test_filter_confidence_PSM (data):
    print('**********************************')
    print('\ntest filter_confidence_psm\n')
    len0, len1, len2 = len(data[0]), len(data[1]), len(data[2])
    print('num of sheets:', len(data), len0, len1, len2)
    for sheet in data:
        print ([( line['Percolator PEP']) for line in sheet ])
    filtered_data = fe.filter_confidence_PSM(data)
    print ('num of sheets:', len(filtered_data), len(filtered_data[0]), len(filtered_data[1]), len(filtered_data[2]) )
    if (len(filtered_data[0]) != len0 - 1):
        print('error- filter_PSM')
    if (len(filtered_data[1]) != len1 - 1):
        print('error- filter_PSM')
    if (len(filtered_data[2]) != len2 - 1):
        print('error- filter_PSM')
    print('\n')
    return filtered_data


def test_rank_PSM (data):
    '''
    ['XCorr'] > 0.5, ['Percolator q-Value'] < 0.9
    '''
    print('**********************************')
    print('\ntest rank_psm\n')
    len0, len1, len2 = len(data[0]), len(data[1]), len(data[2])
    print('num of sheets:', len(data), len0, len1, len2)
    for sheet in data:
        print ([(line['Percolator PEP'],line['XCorr'], line['Percolator q-Value']) for line in sheet ])
    filtered_data = fe.rank_PSM(data)
    print('num of sheets:', len(filtered_data), len(filtered_data[0]), len(filtered_data[1]), len(filtered_data[2]))
    for sheet in filtered_data:
        print ([(line['Percolator PEP'],line['XCorr'], line['Percolator q-Value']) for line in sheet ])
    if (len(filtered_data[0]) != len0 - 2):
        print('error- filter_PSM', len(filtered_data[0]))
    if (len(filtered_data[1]) != len1 - 4):
        print('error- filter_PSM', len(filtered_data[1]))
    if (len(filtered_data[2]) != len2 - 2):
        print('error- filter_PSM', len(filtered_data[2]))
    print('\n')
    return filtered_data


def test_create_names_dict (data):
    print('**********************************')
    print('\ntest create_names_dict\n')
    mode1 = fe.create_names_dict(data, 1)
    mode2 = fe.create_names_dict(data, 2)
    mode3 = fe.create_names_dict(data, 3)
    res1= [(mode1['SYScQVTHEGSTVEK'] == 2) , (mode1['ATLVcLISDFYPGAVTVAWK'] == 2) , (mode1['ASQGIGSALAWYQQKPGEAPK' ] == 1) , \
           (mode1['TPEVTcVVVDVSHEDPEVQFNWYVDGMEVHNAK'] == 1) ,(mode1['EEPEPLSPELEYIPR'] == 2)]
    print(res1)
    res2 = [(mode2['SYScQVTHEGSTVEK'] == 2), (mode2['ATLVcLISDFYPGAVTVAWK'] == 3), (mode2['ASQGIGSALAWYQQKPGEAPK'] == 2),\
           (mode2['TPEVTcVVVDVSHEDPEVQFNWYVDGMEVHNAK'] == 1), (mode2['EEPEPLSPELEYIPR'] == 4)]
    print(res2)
    res3 = [(mode3[0]['SYScQVTHEGSTVEK'] == 1), (mode3[1]['ATLVcLISDFYPGAVTVAWK'] == 2), (mode3[2]['ASQGIGSALAWYQQKPGEAPK'] == 2),\
           (mode3[1]['TPEVTcVVVDVSHEDPEVQFNWYVDGMEVHNAK'] == 1), (mode3[0]['EEPEPLSPELEYIPR'] == 2), (mode3[2]['ATLVcLISDFYPGAVTVAWK'] == 1), \
            (mode3[2]['EEPEPLSPELEYIPR'] == 2),]
    print(res3)
    #print(mode1)
    #print(mode2)
    #print(mode3)
    print('\n')

    #print((i for i in range(len(res)) if res[i] == True)  , 'error in mode 1')


def test_is_present_in_2_replicates (data):
    print('**********************************')
    print('\ntest is_present_in_2_replicates\n')
    filtered_data = fe.is_present_in_2_replicates(data)
    for sheet in filtered_data:
        print ([line['Annotated Sequence'] for line in sheet ])
    if (len(filtered_data[0]) != 3 or len(filtered_data[1])!= 2 or len(filtered_data[2]) != 4):
        print('error')
    if ((('SYScQVTHEGSTVEK' in line['Annotated Sequence'] for line in filtered_data[0]) and ('SYScQVTHEGSTVEK' in line['Annotated Sequence'] for line in filtered_data[2])) == False):
        print('error')
    if ((('EEPEPLSPELEYIPR' in line['Annotated Sequence'] for line in filtered_data[0]) and ('EEPEPLSPELEYIPR' in line['Annotated Sequence'] for line in filtered_data[2])) == False):
        print('error')
    if ((('ATLVcLISDFYPGAVTVAWK' in line['Annotated Sequence'] for line in filtered_data[1]) and ('ATLVcLISDFYPGAVTVAWK' in line['Annotated Sequence'] for line in filtered_data[2])) == False):
        print('error')
    print('\n')


def test_check_if_appears_in_flow_through (first, second, whoIsFirst) :
    print('**********************************')
    print('\ntest check_if_appears_in_flow_through\n')
    filtered_data, filtered_dict = fe.check_if_appears_in_flow_through(first, second)

    if (whoIsFirst == 0):
        for sheet in filtered_data:
            print([line['Annotated Sequence'] for line in sheet])
        if (len(filtered_data[0]) != 4 or len(filtered_data[1]) != 3 or len(filtered_data[2]) != 1):
            print('error')
        

    if (whoIsFirst == 10):
        for sheet in filtered_data:
            print([line['Annotated Sequence'] for line in sheet])
        if (len(filtered_data[0]) != 1 or len(filtered_data[1]) != 1 or len(filtered_data[2]) != 0):
            print('error')

    return filtered_dict
    print('\n')


def test_load_db(file):
    print('**********************************')
    print('\ntest load_db\n')
    db_dict = db.load_db(file)
    if (len(db_dict) != 5 ):
        print('error')
    print('\n')
    if(db_dict['QVQLQESGPGLVLGPSETLSLTKLGSGGSISSSSYYWGWIRQPPGKGLEWIGSIYYSGSTYYNPSLKSRVTISVDTSKNQFSLKLSSVTAADTAVYYCARLSDYDYDRYWFDPWGQGTLVT'] != 'CARGGAKLGTGFDYW'):
        print('error')
    return db_dict


def test_create_filtered_peptides_files_according_to_cdr3 (non_info_file, info_file, CDR3_info_file, db_dict, peptides_dict):
    db.create_filtered_peptides_files_according_to_cdr3(non_info_file, info_file, CDR3_info_file, db_dict, peptides_dict)
    test_db = {'SDFvcxvrgferwt0 ' : 'DSFSDF' ,\
               'GGTESSFFSFSW': 'aSS' ,\
               'ASRFGSASASAGGDDS' : 'GGGDD', \
               'AASDADDDSEES': 'WEWDS',\
               'GGYYYYfvcxvgtt' : 'DSFSDF', \
               'GGYYYYfdfdfderer': 'aGYYY',\
                'GGTESSFSaadfgfgggSW': 'aSS'}
    test_peptides_dict = {'FVCXV':2,\
                          'dfdfd':3,\
                          'GYYY':2, \
                          'SS':1}
    db.create_filtered_peptides_files_according_to_cdr3('test2_non.txt', 'test2_info.txt', 'test2_cdr3.txt', test_db,
                                                        test_peptides_dict)
    print('test2 files:\n'+
          'non: GYYY,\n'+
          'info: FVCXV, dfdfd\n'+
          'cdr3: SS')





if __name__ == '__main__':
    day0 = create_data_day_0()
    filtered_data1 = test_filter_confidence_PSM(day0)
    filtered_data2 = test_rank_PSM (filtered_data1)
    #filtered_data3 = test_rank_PSM(day0)
    test_create_names_dict(day0)
    test_is_present_in_2_replicates(day0)
    day10 = create_data_day_10()
    peptides_dict_for_test = test_check_if_appears_in_flow_through(day0, day10, 0)
    peptides_dict = test_check_if_appears_in_flow_through(day10, day0, 10)
    dbd = test_load_db('IBD_001_D10_MBC IGH-test.fasta')
    test_create_filtered_peptides_files_according_to_cdr3('test_non.txt', 'test_info.txt', 'test_cdr3.txt', dbd,
                                                          peptides_dict_for_test)
