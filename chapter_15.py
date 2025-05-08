
# Chapter 15: Load Balancing & Horizontal Scaling

# Example for load balancer configuration with NGINX
server {
    listen 80;
    server_name myapp.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
    