FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf

RUN if [ ! -d /log ]; then mkdir /log; fi

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]