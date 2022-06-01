% plot multiple robots

% % using matlab robotics tookit (doesnt work)
% n_robots = 10;
% robots = rigidBodyTree.empty(0,n_robots);
% joints = zeros(3,n_robots);
% for i = 1:n_robots
%     joints(:,i) = randn(3,1) * pi/2;
%     robots(i,:) = loadrobot("abbIrb120T","DataFormat","column","Gravity",joints(:,i));
%     show(robots(i));
%     hold on
% end
% robots1 = loadrobot("abbIrb120T","DataFormat","column","Gravity",[0,-pi/2, pi]);
% show(robots1);
% hold on
% robots2 = loadrobot("abbIrb120T","DataFormat","column","Gravity",[0,pi/2, pi]);
% show(robots2);

% using peter corke's


n_robots = 10;
robots = rigidBodyTree.empty(0,n_robots);
joints = zeros(7,n_robots);
for i = 1:n_robots
    joints(:,i) = randn(7,1) * pi/2;
    robots(i,:) = loadrobot("kinovaGen3", "joints", joints(:,i));
    % robots(i,:) = loadrobot("abbIrb120T","DataFormat","column","Gravity",joints(:,i));
    show(robots(i))
    hold on
end

% 
% kin = loadrobot("kinovaGen3");
% fan = loadrobot("fanucLRMate200ib");
% show(kin)
% hold on
% show(fan)
