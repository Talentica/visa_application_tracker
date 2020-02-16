--Create Employees table
CREATE TABLE Employees (
	employeeId bigserial PRIMARY KEY,
	firstName varchar(50) NOT NULL,
	lastName varchar(50) NOT NULL,
	email varchar(255) UNIQUE NOT NULL,
	managerId bigint,
	dateCreated date,
	dateModified date,
	FOREIGN KEY (managerId)
	REFERENCES Employees(employeeId)
);

--Create Roles table
CREATE TABLE Roles (
	roleId serial PRIMARY KEY,
	roleName varchar(50) NOT NULL
);

--Create EmployeeRoles table
CREATE TABLE EmployeeRoles (
	Id bigserial PRIMARY KEY,
	employeeId bigint REFERENCES Employees(employeeId) ON DELETE CASCADE,
	roleId int REFERENCES Roles(roleId),
	dateCreated date,
	dateModified date
);

--Create ApplicationStatus table
CREATE TABLE ApplicationStatus (
	statusId serial PRIMARY KEY,
	status varchar(100) NOT NULL
);

--Create VisaApplications table
CREATE TABLE VisaApplications (
	applicationId bigserial PRIMARY KEY,
	employeeId bigint REFERENCES Employees(employeeId) ON DELETE CASCADE,
	initiatedBy bigint REFERENCES Employees(employeeId),
	ActionPendingOn bigint REFERENCES Employees(employeeId),
	statusId int REFERENCES ApplicationStatus(statusId),
	dateCreated date,
	dateModified date
);

--Create ApplicationHistory table
CREATE TABLE ApplicationHistory (
	applicationHistoryId bigserial PRIMARY KEY,
	applicationId bigserial REFERENCES VisaApplications(applicationId) ON DELETE CASCADE,
	ActionPendingOn bigint REFERENCES Employees(employeeId),
	statusId int REFERENCES ApplicationStatus(statusId),
	dateCreated date
);

--Instead of updating this table, insert into this and update ActiveEmailContent for correct log maintenance
--Create EmailContent table
CREATE TABLE EmailContent (
	emailContentId serial PRIMARY KEY,
	content text NOT NULL
);

--This table maps which email to send to which roles on status change. Seperated out from email content for constraint and logging purpose
--Create EmailContent table.
CREATE TABLE ActiveEmailContent (
	emailContentId int REFERENCES EmailContent(emailContentId),
	statusId int REFERENCES ApplicationStatus(statusId),
	roleId int REFERENCES Roles(roleId),
	UNIQUE (emailContentId, statusId, roleId)
);

--Create EmailLogs table
CREATE TABLE EmailLogs (
	logId serial PRIMARY KEY,
	emailContentId int REFERENCES EmailContent(emailContentId),
	applicationHistoryId bigint REFERENCES ApplicationHistory(applicationHistoryId) ON DELETE CASCADE,
	sentTo bigint REFERENCES Employees(employeeId),
	sentToEmail varchar(255) NOT NULL --In case employee email changes
);