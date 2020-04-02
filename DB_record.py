
class DB_record:

    def __init__(self,db_num, seq, ibd, chain_type, iso_type, cdr3, IGHV,  IGHD, IGHJ, counts, intensity_for_each_rep = None ):
        self.db_num = db_num
        self.seq = seq
        self.ibd = ibd
        self.chain_type = chain_type
        self.iso_type = iso_type
        self.cdr3 = cdr3
        self.cdr3_start = -1
        self.cdr3_end = -1
        self.IGHV = IGHV
        self.IGHD = IGHD
        self.IGHJ = IGHJ
        self.counts = counts
        self.intensity_for_each_rep = intensity_for_each_rep
        self.avg_counts = counts / len(self.intensity_for_each_rep) if intensity_for_each_rep != None else self.counts
        self.frequency = 0





