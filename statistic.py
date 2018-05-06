
class Statistic:
    # statistic calculation
    def __init__(self,data):  # initialization with data points
        self.data = data
        
    def mean(self):
        return sum(self.data)/len(self.data)

    def  p_variance(self):
        myu = self.mean()
        sq_diff_sum = 0
        for x in self.data:
            sq_diff_sum += (x-myu)**2
        return sq_diff_sum/len(self.data)

    def s_variance(self):
        myu = self.mean()
        sq_diff_sum = 0
        for x in self.data:
            sq_diff_sum += (x-myu)**2
        return sq_diff_sum/(len(D)-1)

    def std_deviation(self):
        sigma_sq = self.p_variance()
        return (sigma_sq)**0.5

