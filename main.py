import numpy as np

class tree_formatter:
    
    def __init__(self):
        self.file_name = 'tree.txt'
        self.directory_names = []
        self.directory_depth = []

    def clear_tree_tex_file(self):
        with open('tree.tex', 'w') as f:
            f.write('')

    def _read_in_tree(self):
        with open(self.file_name, 'r') as f:
            tree = f.read()
        return tree
    
    def extract_file_names(self):
        tree = self._read_in_tree()
        tree = tree.split('\n')
        tree = [i for i in tree if i]
        tree = [i.split(' ') for i in tree]
        return tree
    
    def determine_depth(self, array):
        shape = []
        for i in array:
            shape.append(len(i))
        return shape
    
    def set_directory_depth(self, depth_array):
        self.directory_depth = depth_array

    def set_directory_names(self, names_array):
        names = []
        for i in names_array:
            names.append(self._add_dash_before_under_score(i[-1]))
        self.directory_names = names

    def create_latex_file(self):
        with open('tree.tex', 'w') as f:
            f.write('\\documentclass{article}\n')

    def create_tree_structure_file(self):
        with open('tree.tex', 'a') as f:
            f.write('begin{forest} \n')
            f.write('for tree={\n')
            f.write('    font=\\ttfamily,\n')
            f.write("    grow'=0,\n")
            f.write('    child anchor=west,\n')
            f.write('    parent anchor=south,\n')
            f.write('    anchor=west,\n')
            f.write('    calign=first,\n')
            f.write('    edge path={\n')
            f.write('      \\noexpand\\path [draw, \\forestoption{edge}]\n')
            f.write('      (!u.south west) +(7.5pt,0) |- node[fill,inner sep=1.25pt] {} (.child anchor)\\forestoption{edge label};\n')
            f.write('    },\n')
            f.write('    before typesetting nodes={\n')
            f.write('      if n=1\n')
            f.write('        {insert before={[,phantom]}}\n')
            f.write('        {}\n')
            f.write('    },\n')
            f.write('    fit=band,\n')
            f.write('    before computing xy={l=15pt},\n')
            f.write('  }\n')

    def _return_depth_levels(self):
        depth_levels = sorted(np.unique(self.directory_depth))
        reduced_depth_levels = []
        for lines in self.directory_depth:
            reduced_depth_levels.append(depth_levels.index(lines))
        return reduced_depth_levels
    
    def _add_dash_before_under_score(self, string):
            if '_' in string:
                return string.replace('_', '\_')
            else:
                return string

    def append_directory_structure(self):
        depth_levels = self._return_depth_levels()

        with open('tree.tex', 'a') as f:
            for idx,values in enumerate(depth_levels):
                if idx == len(depth_levels)-1:
                    f.write(' {}   ]\n'.format(self.directory_names[idx]))
                elif idx == 0:
                    f.write('    [ {} \n'.format(self.directory_names[idx]))
                else:
                    if depth_levels[idx+1] > depth_levels[idx]:
                        f.write('    [ {} \n'.format(self.directory_names[idx]))
                    elif depth_levels[idx+1] < depth_levels[idx]:
                        f.write('    [{}] ]\n'.format(self.directory_names[idx]))
                    else:
                        f.write('[{}]'.format(self.directory_names[idx]))
            f.write('\end{forest}\n')

if __name__ == '__main__':
    tf = tree_formatter()
    tf.clear_tree_tex_file()
    tree = tf.extract_file_names()
    tf.set_directory_depth(tf.determine_depth(tree))
    tf.set_directory_names(tree)
    tf.create_tree_structure_file()
    tf.append_directory_structure()
