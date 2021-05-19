FROM node:15-slim

# Start Cypress installation
RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install --no-install-recommends -y libgtk2.0-0 wget libgtk-3-0 libnss3 libasound2 xauth xvfb \
       libgconf-2-4 fonts-arphic-bkai00mp fonts-arphic-bsmi00lp fonts-arphic-gbsn00lp libnotify-dev \
       libgbm-dev fonts-arphic-ukai zip fonts-arphic-uming ttf-wqy-zenhei ca-certificates \
       libxss1 fonts-liberation libappindicator3-1 xdg-utils ttf-wqy-microhei xfonts-wqy \
       libxtst6 g++ build-essential fonts-arphic-gkai00mp \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get upgrade

ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

ENV CHROME_VERSION=86.0.4240.193

RUN wget -O /usr/src/google-chrome-stable.deb "http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}-1_amd64.deb" \
  && dpkg -i /usr/src/google-chrome-stable.deb \
  && apt-get install -f -y \
  && rm -f /usr/src/google-chrome-stable.deb

RUN google-chrome --version

# disable shared memory X11 affecting Cypress v4 and Chrome
# https://github.com/cypress-io/cypress-docker-images/issues/270
ENV QT_X11_NO_MITSHM=1
ENV _X11_NO_MITSHM=1
ENV _MITSHM=0

ENV USERNAME=node

ENV CYPRESS_CACHE_FOLDER=/home/${USERNAME}/Cypress

RUN mkdir -p $CYPRESS_CACHE_FOLDER && chown ${USERNAME}:${USERNAME} -R $CYPRESS_CACHE_FOLDER \
    && npm install --global --unsafe-perms pm2 wait-on
# Cypress installation completed

ENV APP_ROOT /app/workspace

WORKDIR ${APP_ROOT}

RUN chown ${USERNAME}:${USERNAME} -R ${APP_ROOT}

USER ${USERNAME}

COPY --chown=${USERNAME} package.json yarn.lock ./

RUN yarn install

COPY --chown=${USERNAME} . ${APP_ROOT}

CMD [ "yarn", "dev" ]
