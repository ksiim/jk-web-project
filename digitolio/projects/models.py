from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

tag_image_dict = {
    "DataScience": "cpp0.svg",
    "ML": "cpp1.svg",
    "AI": "cpp2.svg",
    "DataAnalysis": "cpp3.svg",
    "DataProcessing": "cpp4.svg",
    "FeatureExtraction": "cpp5.svg",
    "DataModeling": "csharp0.svg",
    "MLAlgorithms": "csharp1.svg",
    "DeepLearning": "csharp2.svg",
    "NeuralNetworks": "csharp3.svg",
    "RegressionAnalysis": "csharp4.svg",
    "DataClustering": "csharp5.svg",
    "DataVisualization": "java0.svg",
    "BigData": "java1.svg",
    "DataPreprocessing": "java2.svg",
    "RecommendationSystems": "java3.svg",
    "UnsupervisedLearning": "java4.svg",
    "SupervisedLearning": "kotlin0.svg",
    "TechnicalDataAnalysis": "kotlin1.svg",
    "ProbabilityTheory": "kotlin2.svg",
    "Statistics": "kotlin3.svg",
    "BusinessIntelligence": "kotlin4.svg",
    "TimeSeriesAnalysis": "python0.svg",
    "ModelOptimization": "python1.svg",
    "CloudComputing": "python2.svg",
    "ImageAnalysis": "python3.svg",
    "PredictiveAnalytics": "python4.svg",
    "ProcessAutomation": "ruby0.svg",
    "DistributedSystems": "ruby1.svg",
    "SQL": "ruby2.svg",
    "Regularization": "ruby3.svg",
    "AlgorithmOptimization": "ruby4.svg"
}


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
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')
    programming_language = models.TextField(choices=PROGRAMMING_LANGUAGES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    link_on_code = models.CharField(max_length=255, verbose_name='Ссылка на гитхаб')
    grade = models.IntegerField(null=True, verbose_name='Оценка')
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_first_tag_image(self):
        default_image = "cpp0.svg"
        if self.tags.exists():
            first_tag = self.tags.first().name
            return f'img/cards/{tag_image_dict.get(first_tag, default_image)}'
        return f'img/cards/{default_image}'