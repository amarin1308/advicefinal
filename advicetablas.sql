CREATE TABLE `devices` (
  `id` varchar(16) NOT NULL,
  `model` varchar(30) NOT NULL,
  `brand` varchar(20) NOT NULL,
  `stock` smallint(6) NOT NULL,
  `price` float NOT NULL,
  `processor` varchar(50) NOT NULL,
  `ram` tinyint(4) NOT NULL,
  `graphic_card` varchar(30) NOT NULL,
  `storage` smallint(6) NOT NULL,
  `registered` timestamp NOT NULL DEFAULT current_timestamp(),
  `modified` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `devices_images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `device` varchar(16) NOT NULL,
  `device_image_size` int(11) NOT NULL,
  `device_image_type` varchar(20) NOT NULL,
  `device_image_data` longblob NOT NULL,
  `registered` timestamp NOT NULL DEFAULT current_timestamp(),
  `modified` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_dvc_images_devices` (`device`),
  CONSTRAINT `fk_dvc_images_devices` FOREIGN KEY (`device`) REFERENCES `devices` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `dt_invoice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_invoice` int(11) DEFAULT NULL,
  `id_device` varchar(16) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `taxes` float DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_dt_invoice_devices` (`id_device`),
  KEY `fk_dt_invoice_id_invoice` (`id_invoice`),
  CONSTRAINT `fk_dt_invoice_devices` FOREIGN KEY (`id_device`) REFERENCES `devices` (`id`),
  CONSTRAINT `fk_dt_invoice_id_invoice` FOREIGN KEY (`id_invoice`) REFERENCES `invoice` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `dt_shop_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_sp` int(11) NOT NULL,
  `id_device` varchar(16) NOT NULL,
  `qty` smallint(6) NOT NULL,
  `taxes` float DEFAULT NULL,
  `price` float DEFAULT NULL,
  `registered` timestamp NOT NULL DEFAULT current_timestamp(),
  `modified` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_shop_cart_devices` (`id_device`),
  KEY `fk_shop_cart_id_sp` (`id_sp`),
  CONSTRAINT `fk_shop_cart_devices` FOREIGN KEY (`id_device`) REFERENCES `devices` (`id`),
  CONSTRAINT `fk_shop_cart_id_sp` FOREIGN KEY (`id_sp`) REFERENCES `shop_cart` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `invoice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_token` varchar(8) NOT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_invoice_user_token` (`user_token`),
  CONSTRAINT `fk_invoice_user_token` FOREIGN KEY (`user_token`) REFERENCES `users` (`token`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `shop_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_token` varchar(8) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_shop_cart_users` (`user_token`),
  CONSTRAINT `fk_shop_cart_users` FOREIGN KEY (`user_token`) REFERENCES `users` (`token`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `users` (
  `token` varchar(8) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `role` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `registered` timestamp NOT NULL DEFAULT current_timestamp(),
  `modified` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`token`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `users_images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(8) NOT NULL,
  `user_image_name` varchar(100) NOT NULL,
  `user_image_size` int(11) NOT NULL,
  `user_image_type` varchar(20) NOT NULL,
  `user_image_data` longblob NOT NULL,
  `registered` timestamp NOT NULL DEFAULT current_timestamp(),
  `modified` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `user` (`user`),
  CONSTRAINT `fk_usr_images_users` FOREIGN KEY (`user`) REFERENCES `users` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `users_admin` (
  `token` varchar(8) NOT NULL,
  `username` varchar(30) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `registered` timestamp NOT NULL DEFAULT current_timestamp(),
  `modified` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`token`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
*/;
