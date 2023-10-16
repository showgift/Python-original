# 在函数中修改列表
# 禁止修改列表内容 --> function_name(list_name[:]) / 1.使用列表的切片副本，不会修改原列表 2.也可以复制原列表到新列表
# 原代码
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\n The following models have been printed")
for completed_model in completed_models:
    print(completed_model)


# 使用函数简化代码，使代码有序（有重复操作的代码块可以定义一个函数替代）
def print_model(unprinted_designs, completed_models):
    """模拟打印，模拟转移"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """模拟打印已转移"""
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_model(unprinted_designs, completed_models)
print("\n The following models have been printed")
show_completed_models(completed_models)
