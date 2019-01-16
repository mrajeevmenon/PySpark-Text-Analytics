from __future__ import division
import math

class ClassificationMetrics :
    
    def __fix_division__(self, numerator, denominator) :
        if denominator == 0 :
            return 0 # return 0 instead of throwing error
        else :
            return numerator/denominator
        
    def recall_rate(self, tp, fn) :
        """
        Recall/Senstivity Rate  
        
        Params:
        --------
        tp - number, True Positives
        fn - number, False Negatives
        
        Return :
        --------
            Recall rate in percentage. Float rounded to 3 decimal places
        """
        return round(self.__fix_division__(tp, tp+fn) * 100, 3)
    
    def precision_rate(self, tp, fp) :
        """
        Precision Rate  
        
        Params:
        --------
        tp - number, True Positives
        fp - number, False Positives
        
        Return :
        --------
            Precision rate in percentage. Float rounded to 3 decimal places
        """
        return round(self.__fix_division__(tp, tp+fp) * 100, 3)
    
    def false_discovery_rate(self, tp, fp) :
        """
        False Discovery Rate  
        
        Params:
        --------
        tp - number, True Positives
        fp - number, False Positives
        
        Return :
        --------
            False Discovery rate in percentage. Float rounded to 3 decimal places
        """
        return round(self.__fix_division__(fp, tp+fp) * 100, 3)
    
    def false_positive_rate(self, tn, fp) :
        """
        Type I Error/(alpha)/Fall Out/False Positive Rate  
        
        Params:
        --------
        tn - number, True Negatives
        fp - number, False Positives
        
        Return :
        --------
            False Positive rate in percentage. Float rounded to 3 decimal places
        """
        return round(self.__fix_division__(fp, fp+tn) * 100, 3)
    
    def false_negative_rate(self, tp, fn) :
        """
        Type II Error/(beta)/False Negative Rate  
        
        Params:
        --------
        tp - number, True Positives
        fn - number, False Negatives
        
        Return :
        --------
            False Negatives rate in percentage. Float rounded to 3 decimal places
        """
        return round(self.__fix_division__(fn, tp+fn) * 100, 3)
    
    def true_discovery_rate(self, tn, fn) :
        """
        True Discovery Rate  
        
        Params:
        --------
        tn - number, True Negatives
        fn - number, False Negatives
        
        Return :
        --------
            False Discovery rate in percentage. Float rounded to 3 decimal places
        """
        return round(self.__fix_division__(fn, tn+fn) * 100, 3)
    
    def negative_predictive_rate(self, tn, fn) :
        """
        Negative Predective Rate  
        
        Params:
        --------
        tn - number, True Negatives
        fn - number, False Negatives
        
        Return :
        --------
            Negative Predective rate in percentage. Float rounded to 3 decimal places
        """
        return round(self.__fix_division__(tn, tn+fn) * 100, 3)
    
    def specificity(self, tn, fp) :
        """
        Specificity / True Negative Rate  
        
        Params:
        --------
        tn - number, True Negatives
        fp - number, False Positives
        
        Return :
        --------
            Specificity/True Negative Rate  in percentage. Float rounded to 3 decimal places
        """
        return round(self.__fix_division__(tn, tn+fp) * 100, 3)
    
    def accuracy(self, tp, tn, fp, fn) :
        """
        Accuracy  
        
        Params:
        --------
        tp - number, True Positives
        tn - number, True Negatives
        fp - number, False Positives
        fn - number, False Negatives
        
        Return :
        --------
            Negative Predective rate in percentage. Float rounded to 3 decimal places
        """
        return round(self.__fix_division__(tp+tn, (tp+tn+fp+fn) * 100), 3)
    
    def f1_score(self, tp, fp, fn) :
        """
        F1-Score / F Measure / Sorensen-Dice Index  
        
        Params:
        --------
        tp - number, True Positives
        fp - number, False Positives
        fn - number, False Negatives
        
        Return :
        --------
            F1 Score. Float rounded to 3 decimal places
        """
        return round(self.__fix_division__(2*tp, ((2*tp)+fp+fn)), 3)
    
    def matt_corr(self, tp, tn, fp, fn) :
        """
        Mathews Correlation Coefficients  
        
        Params:
        --------
        tp - number, True Positives
        fp - number, False Positives
        fn - number, False Negatives
        
        Return :
        --------
            Mathews Correlation Coefficient. Float rounded to 3 decimal places
        """
        numer = (tp*tn) - (fp*fn)
        deno = math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
        return round(self.__fix_division__(numer, deno), 3)
    
    
    def print_all_metrics(self, tp, tn, fp, fn) :
        """
            Prints metrics like Senstivity, Type I, Type II, Precision, Accuracy, F1-Score, Matt Corr,
            False Discovery, True Discovery, Negative Predictive, and Specificity.
        """
        print ("Recall/Senstivity Rate : ", self.recall_rate(tp,fn))
        print ("Precision Rate : ", self.precision_rate(tp,fp))
        print ("Accuracy : ", self.accuracy(tp, tn, fp, fn))
        print ("F1-Score / F Measure / Sorensen-Dice Index :",  self.f1_score(tp, fp, fn))
        print ("Mathews Correlation Coefficients :", self.matt_corr(tp, tn, fp, fn))
        print ("Type I Error/(alpha)/Fall Out/False Positive Rate : ", self.false_positive_rate(tn,fp))
        print ("Type II Error/(beta)/False Negative Rate :", self.false_negative_rate(tp, fn))
        print ("True Discovery Rate :", self.true_discovery_rate(tn, fn))
        print ("False Discovery Rate :", self.false_discovery_rate(tp, fp))
        print ("Negative Predictive Rate :", self.negative_predictive_rate(tn, fn))
        print ("Specificity / True Negative Rate :", self.specificity(tn, fp))