-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.3-beta1
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: new_database | type: DATABASE --
-- DROP DATABASE IF EXISTS new_database;
--CREATE DATABASE new_database;
-- ddl-end --


-- object: public.estudiantes | type: TABLE --
-- DROP TABLE IF EXISTS public.estudiantes CASCADE;
CREATE TABLE public.estudiantes (
	codigo_estudiante integer NOT NULL,
	nombre text NOT NULL,
	apellidos text NOT NULL,
	direccion text NOT NULL,
	pais text NOT NULL,
	telefono bigint NOT NULL,
	email text NOT NULL,
	creditos_aprobados integer NOT NULL,
	codigo_erasmus_universidades integer,
	CONSTRAINT estudiantes_pk PRIMARY KEY (codigo_estudiante)

);
-- ddl-end --
COMMENT ON TABLE public.estudiantes IS E'Guarda los estudiantes que solicitan becas para realizar estancias en universidades distintas de donde están matriculados.';
-- ddl-end --
COMMENT ON COLUMN public.estudiantes.codigo_estudiante IS E'Guarda el código del estudiante.';
-- ddl-end --
COMMENT ON COLUMN public.estudiantes.nombre IS E'Guarda el nombre del estudiante';
-- ddl-end --
COMMENT ON COLUMN public.estudiantes.apellidos IS E'Guarda los apellidos del estudiante.';
-- ddl-end --
COMMENT ON COLUMN public.estudiantes.direccion IS E'Guarda la dirección del estudiante.';
-- ddl-end --
COMMENT ON COLUMN public.estudiantes.pais IS E'Guarda el país de nacimiento del estudiante. Hay 50 países Europeos y uno de ellos debe ser España en la base de datos.';
-- ddl-end --
COMMENT ON COLUMN public.estudiantes.telefono IS E'uarda el teléfono de contacto del estudiante.';
-- ddl-end --
COMMENT ON COLUMN public.estudiantes.email IS E'Guarda el email del estudiante.';
-- ddl-end --
COMMENT ON COLUMN public.estudiantes.creditos_aprobados IS E'Guarda el número de créditos conseguidos/aprobados en su carrera. Para disfrutar de una beca deben ser mayores o iguales a 60 ECTS y menores o iguales de 220.';
-- ddl-end --
ALTER TABLE public.estudiantes OWNER TO postgres;
-- ddl-end --

-- object: public.universidades | type: TABLE --
-- DROP TABLE IF EXISTS public.universidades CASCADE;
CREATE TABLE public.universidades (
	codigo_erasmus integer NOT NULL,
	nombre text NOT NULL,
	direccion text NOT NULL,
	pais text NOT NULL,
	telefono bigint NOT NULL,
	email text NOT NULL,
	CONSTRAINT universidades_pk PRIMARY KEY (codigo_erasmus)

);
-- ddl-end --
COMMENT ON TABLE public.universidades IS E'Guarda la información sobre las Universidades que oferan becas e instancias.';
-- ddl-end --
COMMENT ON COLUMN public.universidades.codigo_erasmus IS E'Guarda el código Erasmus de la Universidad';
-- ddl-end --
COMMENT ON COLUMN public.universidades.nombre IS E'Guarda el nombre de la Universidad';
-- ddl-end --
COMMENT ON COLUMN public.universidades.direccion IS E'Guarda la dirección de la Universidad en cuestión.';
-- ddl-end --
COMMENT ON COLUMN public.universidades.pais IS E'Guarda el pais de la Universidad. Hay 50 paises Europeos en la base de datos y uno de ellos debe de ser España.';
-- ddl-end --
COMMENT ON COLUMN public.universidades.telefono IS E'Guarda el teléfono de información de la Universidad';
-- ddl-end --
COMMENT ON COLUMN public.universidades.email IS E'Guarda el email de contacto de la Universidad en cuestión.';
-- ddl-end --
ALTER TABLE public.universidades OWNER TO postgres;
-- ddl-end --

-- object: public.asignaturas | type: TABLE --
-- DROP TABLE IF EXISTS public.asignaturas CASCADE;
CREATE TABLE public.asignaturas (
	codigo_asignatura integer NOT NULL,
	nombre text NOT NULL,
	creditos integer NOT NULL,
	tipo text NOT NULL,
	universidad integer,
	CONSTRAINT asignaturas_pk PRIMARY KEY (codigo_asignatura)

);
-- ddl-end --
COMMENT ON TABLE public.asignaturas IS E'Guardan las asignaturas que se ofertan en todas las Universidades.';
-- ddl-end --
COMMENT ON COLUMN public.asignaturas.codigo_asignatura IS E'Guarda el código de asignatura';
-- ddl-end --
COMMENT ON COLUMN public.asignaturas.nombre IS E'Guarda el nombre de la asignatura';
-- ddl-end --
COMMENT ON COLUMN public.asignaturas.creditos IS E'Guarda el número de créditos ECTS de la asignatura. En este campo se deben de gurdar entre 4 y 12 ECTS, ambos valores incluidos.';
-- ddl-end --
COMMENT ON COLUMN public.asignaturas.tipo IS E'Puede ser básica, obligatoria, transversal, optativa.';
-- ddl-end --
ALTER TABLE public.asignaturas OWNER TO postgres;
-- ddl-end --

-- object: public.estancias | type: TABLE --
-- DROP TABLE IF EXISTS public.estancias CASCADE;
CREATE TABLE public.estancias (
	fecha_inicio date NOT NULL,
	fecha_fin date NOT NULL,
	tipo_beca text NOT NULL,
	duracion char(1) NOT NULL,
	cuantia real NOT NULL,
	estudiante integer NOT NULL,
	universidad integer NOT NULL,
	CONSTRAINT estancias_pk PRIMARY KEY (estudiante,universidad)

);
-- ddl-end --
COMMENT ON COLUMN public.estancias.fecha_inicio IS E'Guarda la fecha de inicio de la estancia';
-- ddl-end --
COMMENT ON COLUMN public.estancias.fecha_fin IS E'Guarda la fecha de fin de la estancia.';
-- ddl-end --
COMMENT ON COLUMN public.estancias.tipo_beca IS E'Guarda el tipo de beca de la estancia. Pueden ser becas del tipo:\n\n- KA103\n- KA107\n- MIT\n- Franklin\n- SICUE\n- Global';
-- ddl-end --
COMMENT ON COLUMN public.estancias.duracion IS E'Puede ser:\n A --> Anual\n 1 --> cuatrimestre 1\n 2 --> cuatrimestre 2';
-- ddl-end --
COMMENT ON COLUMN public.estancias.cuantia IS E'Guarda la cuantía de la beca recibida para realizar la estancia. Esas cuantía varía entre 500 y 2000 euros, ambos valores incluidos.';
-- ddl-end --
ALTER TABLE public.estancias OWNER TO postgres;
-- ddl-end --

-- object: public.convalidaciones | type: TABLE --
-- DROP TABLE IF EXISTS public.convalidaciones CASCADE;
CREATE TABLE public.convalidaciones (
	nota_destino char(2) NOT NULL,
	nota_origen real NOT NULL,
	fecha date NOT NULL,
	estudiante_estancias integer NOT NULL,
	universidad_estancias integer NOT NULL,
	asignatura_origen integer NOT NULL,
	asignatura_destino integer NOT NULL,
	CONSTRAINT convalidaciones_pk PRIMARY KEY (estudiante_estancias,universidad_estancias,asignatura_origen,asignatura_destino)

);
-- ddl-end --
COMMENT ON TABLE public.convalidaciones IS E'Guardan las convalidaciones que se han producido en todas las estancias.';
-- ddl-end --
COMMENT ON COLUMN public.convalidaciones.nota_destino IS E'Guarda la nota de la asignatura cursada en la Universidad de destino. Puede ser: A+,A,A-,B+,B,B-,C+,C,C-,D+,D,D-,E,F';
-- ddl-end --
COMMENT ON COLUMN public.convalidaciones.nota_origen IS E'Guarda la nota en la universidad de origen. La transformación de notas corresponde:\nA+ --> 10\nA -->9.8\nA- --> 9.5 \nB+ --> 9.0\nB --> 8.5\nB- --> 8.0\nC+ --> 7.5\nC -->7.3\nC- --> 7.0\nD+ -->6.5\nD -->6.0\nD- -->5.5\nE-->5.0\nF-->4.0';
-- ddl-end --
COMMENT ON COLUMN public.convalidaciones.fecha IS E'Guarda la fecha en la que se produce la convalidación.';
-- ddl-end --
ALTER TABLE public.convalidaciones OWNER TO postgres;
-- ddl-end --

-- object: universidades_fk | type: CONSTRAINT --
-- ALTER TABLE public.estudiantes DROP CONSTRAINT IF EXISTS universidades_fk CASCADE;
ALTER TABLE public.estudiantes ADD CONSTRAINT universidades_fk FOREIGN KEY (codigo_erasmus_universidades)
REFERENCES public.universidades (codigo_erasmus) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: universidades_fk | type: CONSTRAINT --
-- ALTER TABLE public.asignaturas DROP CONSTRAINT IF EXISTS universidades_fk CASCADE;
ALTER TABLE public.asignaturas ADD CONSTRAINT universidades_fk FOREIGN KEY (universidad)
REFERENCES public.universidades (codigo_erasmus) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: estudiantes_fk | type: CONSTRAINT --
-- ALTER TABLE public.estancias DROP CONSTRAINT IF EXISTS estudiantes_fk CASCADE;
ALTER TABLE public.estancias ADD CONSTRAINT estudiantes_fk FOREIGN KEY (estudiante)
REFERENCES public.estudiantes (codigo_estudiante) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: universidades_fk | type: CONSTRAINT --
-- ALTER TABLE public.estancias DROP CONSTRAINT IF EXISTS universidades_fk CASCADE;
ALTER TABLE public.estancias ADD CONSTRAINT universidades_fk FOREIGN KEY (universidad)
REFERENCES public.universidades (codigo_erasmus) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: estancias_fk | type: CONSTRAINT --
-- ALTER TABLE public.convalidaciones DROP CONSTRAINT IF EXISTS estancias_fk CASCADE;
ALTER TABLE public.convalidaciones ADD CONSTRAINT estancias_fk FOREIGN KEY (estudiante_estancias,universidad_estancias)
REFERENCES public.estancias (estudiante,universidad) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: asignaturas_fk | type: CONSTRAINT --
-- ALTER TABLE public.convalidaciones DROP CONSTRAINT IF EXISTS asignaturas_fk CASCADE;
ALTER TABLE public.convalidaciones ADD CONSTRAINT asignaturas_fk FOREIGN KEY (asignatura_origen)
REFERENCES public.asignaturas (codigo_asignatura) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: asignaturas_fk1 | type: CONSTRAINT --
-- ALTER TABLE public.convalidaciones DROP CONSTRAINT IF EXISTS asignaturas_fk1 CASCADE;
ALTER TABLE public.convalidaciones ADD CONSTRAINT asignaturas_fk1 FOREIGN KEY (asignatura_destino)
REFERENCES public.asignaturas (codigo_asignatura) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --


