from skimage import data, segmentation, filters, color #16dars
from skimage import graph
from matplotlib import pyplot as plt

def weight_boundary(graph, src, dst, n):
    """
    Обработка слияния узлов графа регионов с учетом границ.

    Эта функция вычисляет атрибуты "weight" и "count" для ребра между `n`
    и узлом, образованным после слияния `src` и `dst`.


    Parameters
    ----------
    graph : RAG
        Рассматриваемый граф.
    src, dst : int
        Вершины в графе, которые будут объединены.
    n : int
        Сосед `src` или `dst` или оба.

    Returns
    -------
    data : dict
        Словарь с атрибутами "weight" и "count" для объединенного узла.

    """
    default = {'weight': 0.0, 'count': 0}

    count_src = graph[src].get(n, default)['count']
    count_dst = graph[dst].get(n, default)['count']

    weight_src = graph[src].get(n, default)['weight']
    weight_dst = graph[dst].get(n, default)['weight']

    count = count_src + count_dst
    return {
        'count': count,
        'weight': (count_src * weight_src + count_dst * weight_dst) / count
    }

def merge_boundary(graph, src, dst):
    """Обратный вызов, вызываемый перед слиянием двух узлов.

    В данном случае никаких вычислений не требуется.
    """
    pass

# Загрузка изображения (в данном случае, изображение кофе из встроенных данных skimage)
img = data.coffee()

# Выделение границ на изображении с использованием оператора Собеля
edges = filters.sobel(color.rgb2gray(img))

# Сегментация изображения методом SLIC
labels = segmentation.slic(img, compactness=30, n_segments=400, start_label=1)

# Создание графа регионов на основе границ
g = graph.rag_boundary(labels, edges)

# Отображение начального графа регионов
graph.show_rag(labels, g, img)
plt.title('Исходный RAG')

# Иерархическое слияние регионов
labels2 = graph.merge_hierarchical(labels, g, thresh=0.08, rag_copy=False,
                                   in_place_merge=True,
                                   merge_func=merge_boundary,
                                   weight_func=weight_boundary)

# Отображение графа регионов после иерархического слияния
graph.show_rag(labels, g, img)
plt.title('RAG после иерархического слияния')

# Визуализация конечной сегментации
plt.figure()
out = color.label2rgb(labels2, img, kind='avg', bg_label=0)
plt.imshow(out)
plt.title('Конечная сегментация')

plt.show()
