from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

PROGRAMMING_LANGUAGES = [
    ("Python", "Python"),
    ("JavaScript", "JavaScript"),
    ("Java", "Java"),
    ("Cpp", "C++"),
    ("Csharp", "C#"),
    ("Ruby", "Ruby"),
    ("Golang", "Golang"),
    ("Scala", "Scala"),
]

TAGS = [
    ("DataScience", "Data Science"),
    ("ML", "Машинное обучение"),
    ("AI", "Искусственный интеллект"),
    ("DataAnalysis", "Анализ данных"),
    ("DataProcessing", "Обработка данных"),
    ("FeatureExtraction", "Извлечение признаков"),
    ("DataModeling", "Моделирование данных"),
    ("MLAlgorithms", "Алгоритмы машинного обучения"),
    ("DeepLearning", "Глубокое обучение"),
    ("NeuralNetworks", "Нейронные сети"),
    ("RegressionAnalysis", "Регрессионный анализ"),
    ("DataClustering", "Кластеризация данных"),
    ("DataVisualization", "Визуализация данных"),
    ("BigData", "Большие данные (Big Data)"),
    ("DataPreprocessing", "Предобработка данных"),
    ("RecommendationSystems", "Рекомендательные системы"),
    ("UnsupervisedLearning", "Обучение без учителя"),
    ("SupervisedLearning", "Обучение с учителем"),
    ("TechnicalDataAnalysis", "Технический анализ данных"),
    ("ProbabilityTheory", "Теория вероятностей"),
    ("Statistics", "Статистика"),
    ("BusinessIntelligence", "Бизнес-интеллект"),
    ("TimeSeriesAnalysis", "Анализ временных рядов"),
    ("ModelOptimization", "Оптимизация моделей"),
    ("CloudComputing", "Облачные вычисления"),
    ("ImageAnalysis", "Анализ изображений"),
    ("PredictiveAnalytics", "Предсказательная аналитика"),
    ("ProcessAutomation", "Автоматизация процессов"),
    ("DistributedSystems", "Распределённые системы"),
    ("SQL", "SQL"),
    ("Regularization", "Регуляризация"),
    ("AlgorithmOptimization", "Оптимизация алгоритмов"),
]

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects', verbose_name='Автор', null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='Теги')
    programming_language = models.TextField(choices=PROGRAMMING_LANGUAGES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    # banner = models.CharField(max_length=255)
    link_on_code = models.CharField(max_length=255, verbose_name='Ссылка на гитхаб')
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
