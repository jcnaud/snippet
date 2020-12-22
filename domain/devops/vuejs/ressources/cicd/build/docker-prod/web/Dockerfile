FROM nginx:1.17-alpine

# Copy src
COPY --chown=nginx:nginx jenkins_release/vuejs_devops /home/www
COPY --chown=root:root cicd/build/docker-prod/web/nginx.conf /etc/nginx/conf.d/default.conf
