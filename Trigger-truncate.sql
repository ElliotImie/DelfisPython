 /*
 A faire avant
 SET GLOBAL event_scheduler := 1; 
 */

 create event truncate_49 on schedule every 20  second do truncate usr_49 ;