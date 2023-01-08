


from rapidfuzz import distance
import ast
from os import path
import argparse




class Comparator():

    map_cl : dict = {"<class 'ast.mod'>": 0, "<class 'ast.stmt'>": 1, "<class 'ast.expr'>": 2, "<class 'ast.expr_context'>": 3, "<class 'ast.slice'>": 4, "<class 'ast.boolop'>": 5, "<class 'ast.operator'>": 6, "<class 'ast.unaryop'>": 7, "<class 'ast.cmpop'>": 8, "<class 'ast.comprehension'>": 9, "<class 'ast.excepthandler'>": 10, "<class 'ast.arguments'>": 11, "<class 'ast.arg'>": 12, "<class 'ast.keyword'>": 13, "<class 'ast.alias'>": 14, "<class 'ast.withitem'>": 15, "<class 'ast.type_ignore'>": 16, "<class 'ast.Module'>": 17, "<class 'ast.Interactive'>": 18, "<class 'ast.Expression'>": 19, "<class 'ast.FunctionType'>": 20, "<class 'ast.Suite'>": 21, "<class 'ast.FunctionDef'>": 22, "<class 'ast.AsyncFunctionDef'>": 23, "<class 'ast.ClassDef'>": 24, "<class 'ast.Return'>": 25, "<class 'ast.Delete'>": 26, "<class 'ast.Assign'>": 27, "<class 'ast.AugAssign'>": 28, "<class 'ast.AnnAssign'>": 29, "<class 'ast.For'>": 30, "<class 'ast.AsyncFor'>": 31, "<class 'ast.While'>": 32, "<class 'ast.If'>": 33, "<class 'ast.With'>": 34, "<class 'ast.AsyncWith'>": 35, "<class 'ast.Raise'>": 36, "<class 'ast.Try'>": 37, "<class 'ast.Assert'>": 38, "<class 'ast.Import'>": 39, "<class 'ast.ImportFrom'>": 40, "<class 'ast.Global'>": 41, "<class 'ast.Nonlocal'>": 42, "<class 'ast.Expr'>": 43, "<class 'ast.Pass'>": 44, "<class 'ast.Break'>": 45, "<class 'ast.Continue'>": 46, "<class 'ast.BoolOp'>": 47, "<class 'ast.NamedExpr'>": 48, "<class 'ast.BinOp'>": 49, "<class 'ast.UnaryOp'>": 50, "<class 'ast.Lambda'>": 51, "<class 'ast.IfExp'>": 52, "<class 'ast.Dict'>": 53, "<class 'ast.Set'>": 54, "<class 'ast.ListComp'>": 55, "<class 'ast.SetComp'>": 56, "<class 'ast.DictComp'>": 57, "<class 'ast.GeneratorExp'>": 58, "<class 'ast.Await'>": 59, "<class 'ast.Yield'>": 60, "<class 'ast.YieldFrom'>": 61, "<class 'ast.Compare'>": 62, "<class 'ast.Call'>": 63, "<class 'ast.FormattedValue'>": 64, "<class 'ast.JoinedStr'>": 65, "<class 'ast.Constant'>": 66, "<class 'ast.Attribute'>": 67, "<class 'ast.Subscript'>": 68, "<class 'ast.Starred'>": 69, "<class 'ast.Name'>": 70, "<class 'ast.List'>": 71, "<class 'ast.Tuple'>": 72, "<class 'ast.Load'>": 73, "<class 'ast.Store'>": 74, "<class 'ast.Del'>": 75, "<class 'ast.AugLoad'>": 76, "<class 'ast.AugStore'>": 77, "<class 'ast.Param'>": 78, "<class 'ast.Slice'>": 79, "<class 'ast.ExtSlice'>": 80, "<class 'ast.Index'>": 81, "<class 'ast.And'>": 82, "<class 'ast.Or'>": 83, "<class 'ast.Add'>": 84, "<class 'ast.Sub'>": 85, "<class 'ast.Mult'>": 86, "<class 'ast.MatMult'>": 87, "<class 'ast.Div'>": 88, "<class 'ast.Mod'>": 89, "<class 'ast.Pow'>": 90, "<class 'ast.LShift'>": 91, "<class 'ast.RShift'>": 92, "<class 'ast.BitOr'>": 93, "<class 'ast.BitXor'>": 94, "<class 'ast.BitAnd'>": 95, "<class 'ast.FloorDiv'>": 96, "<class 'ast.Invert'>": 97, "<class 'ast.Not'>": 98, "<class 'ast.UAdd'>": 99, "<class 'ast.USub'>": 100, "<class 'ast.Eq'>": 101, "<class 'ast.NotEq'>": 102, "<class 'ast.Lt'>": 103, "<class 'ast.LtE'>": 104, "<class 'ast.Gt'>": 105, "<class 'ast.GtE'>": 106, "<class 'ast.Is'>": 107, "<class 'ast.IsNot'>": 108, "<class 'ast.In'>": 109, "<class 'ast.NotIn'>": 110, "<class 'ast.ExceptHandler'>": 111, "<class 'ast.TypeIgnore'>": 112}


    
    

    def __init__(self) -> None:
        pass

    def compare_strs(self, s1 : str, s2 : str, preproc_type : int = 1, metric : int = 1) -> float:
        """
        preproc_type - тип препроцессинга строк 
        1 - С заменой (по умолчанию)
        2 - Без замены
        metric - применяемая метрика для степени различия файлов
        1 - Расстояние Дамерау-Левенштейна (по умолчанию)
        2 - Расстояние Левенштейна
        """

        if (preproc_type != 1 and preproc_type != 2):
            raise Exception("Неверный тип препроцессинга")
        if (metric != 1 and metric != 2):
            raise Exception("Неверный тип метрики")



        if preproc_type == 1:
            self.__strs_preproc_map(s1, s2)

            if metric == 1:
                return self.__find_damLewDistance()
            else:
                return self.__find_lewDistance()
            
        else:
            self.__strs_preproc(s1, s2)
            if metric == 1:
                return self.__find_damLewDistance()
            else:
                return self.__find_lewDistance()

        
    def compare_files(self, path1 : str, path2 : str, preproc_type : int = 1, metric : int = 1) -> float:
        if (not path.exists(path1)):
            raise Exception("Неверный путь")
        if (not path.exists(path2)):
            raise Exception("Неверный путь")
            
        
        f1 = open(path1, encoding="utf-8")
        s1 = f1.read()
        f1.close()

        f2 = open(path2, encoding="utf-8")
        s2 = f2.read()
        f2.close()

        return self.compare_files(s1, s2, preproc_type, metric)


                





    
    def __strs_preproc(self, s1 : str, s2 : str) -> None:
        self.s1_cont = ast.dump(ast.parse(s1))
        self.s2_cont = ast.dump(ast.parse(s2))
        
    def __strs_preproc_map(self, s1 : str, s2 : str) -> None:
        tr1 = ast.parse(s1)
        self.s1_cont = []
        for elem in ast.walk(tr1):
            self.s1_cont += [self.map_cl[str(type(elem))]]

        tr2 = ast.parse(s2)
        self.s2_cont = []
        for elem in ast.walk(tr2):
            self.s2_cont += [self.map_cl[str(type(elem))]]
    
    
    def __find_lewDistance(self) -> float:
        return distance.Levenshtein.normalized_distance(self.s1_cont, self.s2_cont)

    def __find_damLewDistance(self) -> float:
        return distance.DamerauLevenshtein.normalized_distance(self.s1_cont, self.s2_cont)

    

def main():
    prs = argparse.ArgumentParser()
    prs.add_argument("input_file", dest = "input_file" help = "file with list of input files")
    prs.add_argument("output_file", dest = "output_file", help = "file with results")
    prs.add_argument("--preproc-type", dest = "preproc_type", help = "the type of preprocessing to be used", default=1)
    prs.add_argument("--metric", dest = "metric", help = "the metric to be used", default=1)

    args = prs.parse_args()


    if (not path.exists(args.input_file)):
        raise Exception("Неверный путь")
        
    if (not path.exists(args.output_file)):
        raise Exception("Неверный путь")
        

    cmp = Comparator()

    f_in = open(args.input_file)
    f_out = open(args.output_file, "w")
    for line in f_in.readlines():
        path1, path2 = line.split()
        k = cmp.compare_files(path1, path2, args.preproc_type, args.metric)
        f_out.write(f"{k}\n")

    
    f_in.close()
    f_out.close()
    



        
if __name__ == "__main__":
    main()