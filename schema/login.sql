-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema schema_login
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `schema_login` ;

-- -----------------------------------------------------
-- Schema schema_login
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `schema_login` DEFAULT CHARACTER SET utf8 ;
USE `schema_login` ;

-- -----------------------------------------------------
-- Table `schema_login`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_login`.`usuario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `schema_login`.`login`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_login`.`login` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `session` INT NULL,
  `usuario_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`, `usuario_id`),
  INDEX `fk_login_usuario_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_login_usuario`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `schema_login`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
