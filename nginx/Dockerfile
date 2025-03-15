# Используем официальный образ Nginx
FROM nginx:latest

# Копируем файл конфигурации Nginx в контейнер
RUN mkdir -p /app/staticfiles

# Копируем статические файлы веб-сайта в директорию для обслуживания
COPY nginx.conf /etc/nginx/nginx.conf

# Открываем порт 80 для HTTP-трафика
EXPOSE 80
