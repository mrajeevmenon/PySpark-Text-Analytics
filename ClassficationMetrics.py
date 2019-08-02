import math

class ClassificationMetrics :
    """
        This helper class will calculate the metrics required for classification 
        like Senstivity, Type I, Type II, Precision, Accuracy, F1-Score, Matt Corr,
        False Discovery, True Discovery, Negative Predictive, and Specificity.
    """
    
    def __init__(self, tp, tn, fp, fn):
        """
        Params:
        --------
        tp - number, True Positives
        tn - number, True Negatives
        fp - number, False Positives
        fn - number, False Negatives
        """
        self.tp = tp
        self.tn = tn
        self.fp = fp
        self.fn = fn
    
    def _fix_division(self, numerator, denominator) :
        if denominator == 0 :
            raise Exception("Error Occurred: Denomintor cannot be ZERO")
        else :
            return numerator/denominator
        
    def recall_rate(self) :
        """
        Recall/Senstivity Rate  

        Return :
        --------
            Recall rate in percentage. Float rounded to 3 decimal places
        """
        return round(self._fix_division(self.tp, self.tp + self.fn) * 100, 3)
    
    def precision_rate(self) :
        """
        Precision Rate  
        
        Return :
        --------
            Precision rate in percentage. Float rounded to 3 decimal places
        """
        return round(self._fix_division(self.tp, self.tp + self.fp) * 100, 3)
    
    def false_discovery_rate(self) :
        """
        False Discovery Rate  
        
        Return :
        --------
            False Discovery rate in percentage. Float rounded to 3 decimal places
        """
        return round(self._fix_division(self.fp, self.tp + self.fp) * 100, 3)
    
    def false_positive_rate(self) :
        """
        Type I Error/(alpha)/Fall Out/False Positive Rate  
        
        Return :
        --------
            False Positive rate in percentage. Float rounded to 3 decimal places
        """
        return round(self._fix_division(self.fp, self.fp + self.tn) * 100, 3)
    
    def false_negative_rate(self) :
        """
        Type II Error/(beta)/False Negative Rate  
        
        Return :
        --------
            False Negatives rate in percentage. Float rounded to 3 decimal places
        """
        return round(self._fix_division(self.fn, self.tp + self.fn) * 100, 3)
    
    def true_discovery_rate(self) :
        """
        True Discovery Rate  
                
        Return :
        --------
            False Discovery rate in percentage. Float rounded to 3 decimal places
        """
        return round(self._fix_division(self.fn, self.tn + self.fn) * 100, 3)
    
    def negative_predictive_rate(self) :
        """
        Negative Predective Rate  
                
        Return :
        --------
            Negative Predective rate in percentage. Float rounded to 3 decimal places
        """
        return round(self._fix_division(self.tn, self.tn + self.fn) * 100, 3)
    
    def specificity(self) :
        """
        Specificity / True Negative Rate  
        
        Return :
        --------
            Specificity/True Negative Rate  in percentage. Float rounded to 3 decimal places
        """
        return round(self._fix_division(self.tn, self.tn + self.fp) * 100, 3)
    
    def accuracy(self) :
        """
        Accuracy  
        
        Return :
        --------
            Negative Predective rate in percentage. Float rounded to 3 decimal places
        """
        return round(self._fix_division(self.tp + self.tn, (self.tp + self.tn + self.fp + self.fn) * 100), 3)
    
    def f1_score(self) :
        """
        F1-Score / F Measure / Sorensen-Dice Index  
        
        Return :
        --------
            F1 Score. Float rounded to 3 decimal places
        """
        return round(self._fix_division(2 * self.tp, ((2 * self.tp) + self.fp + self.fn)), 3)
    
    def matt_corr(self) :
        """
        Mathews Correlation Coefficients  
        
        Return :
        --------
            Mathews Correlation Coefficient. Float rounded to 3 decimal places
        """
        numer = (self.tp * self.tn) - (self.fp * self.fn)
        deno = math.sqrt((self.tp + self.fp) * (self.tp + self.fn) * (self.tn + self.fp) * (self.tn + self.fn))
        return round(self._fix_division(numer, deno), 3)
        
    def print_all_metrics(self) :
        """
            Prints metrics like Senstivity, Type I, Type II, Precision, Accuracy, F1-Score, Matt Corr,
            False Discovery, True Discovery, Negative Predictive, and Specificity.
        """
        print ("Recall/Senstivity Rate : ", self.recall_rate())
        print ("Precision Rate : ", self.precision_rate())
        print ("Accuracy : ", self.accuracy())
        print ("F1-Score / F Measure / Sorensen-Dice Index :",  self.f1_score())
        print ("Mathews Correlation Coefficients :", self.matt_corr())
        print ("Type I Error/(alpha)/Fall Out/False Positive Rate : ", self.false_positive_rate())
        print ("Type II Error/(beta)/False Negative Rate :", self.false_negative_rate())
        print ("True Discovery Rate :", self.true_discovery_rate())
        print ("False Discovery Rate :", self.false_discovery_rate())
        print ("Negative Predictive Rate :", self.negative_predictive_rate())
        print ("Specificity / True Negative Rate :", self.specificity())
